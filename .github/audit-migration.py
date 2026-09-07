"""Audit the port: every variable a pre-port theme declared must have its migrated
token in the ported theme. The mapping is read from index.md so the audit cannot
drift away from the documented one."""
import pathlib
import re
import subprocess
import sys

REPO = str(pathlib.Path(__file__).resolve().parent.parent)
BEFORE = "0a139ff7"

def show(rev, path):
    r = subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def mapping():
    """old variable -> set of -color-* tokens it became ('' = no successor)."""
    text = pathlib.Path(REPO, "index.md").read_text()
    table = text.split("### Migrating a theme from JabRef 5.x")[1].split("## Selection")[0]
    m = {}
    for line in table.split("\n"):
        if not line.startswith("| `"):
            continue
        left, right = [c.strip() for c in line.strip().strip("|").split(" | ")]
        targets = set(re.findall(r"-color-[a-z0-9-]+", right))
        for old in re.findall(r"-(?:jr|fx)-[a-z0-9-]+", left):
            m.setdefault(old, set()).update(targets)
    # The three groups that live in prose below the table.
    for old in re.findall(r"-jr-[a-z0-9-]+", table.split("Three groups do not fit a cell:")[1].split("\n*")[1]):
        m.setdefault(old, set()).update({"-color-fg-default", "-color-fg-emphasis"})
    for old in re.findall(r"-jr-[a-z0-9-]+", "".join(table.split("Three groups do not fit a cell:")[1].split("\n*")[2:])):
        m.setdefault(old, set())          # palette entries and -jr-header-height: no successor
    return m

def declared(css, block=None):
    """Names declared in the whole file, or inside the given @media block."""
    if block:
        m = re.search(r"@media \(prefers-color-scheme: %s\).*?\n\}" % block, css, re.S)
        css = m.group(0) if m else ""
    return set(re.findall(r"^\s+(-[a-z0-9-]+):", css, re.M))

def ancestors(path):
    """Ported file -> [(pre-port path, media block or None)]."""
    name = pathlib.PurePath(path).name
    if "/DinoGirls Themes/" in path:
        dark, light, variant = name[:-4].rsplit("-", 2)[0].split("-")[0], name[:-4].split("-")[1], name[:-4].rsplit("-", 1)[1]
        dvar, lvar = ("greytext", "greytext") if variant == "greytext" else ("whitetext", "blacktext")
        return [(f"themes/DarkTheme/DinoGirls Dark Themes/DARK THEME-{dark}-{dvar}.css", "dark"),
                (f"themes/LightTheme/DinoGirls Light Themes/LIGHT THEME-{light}-{lvar}.css", "light")]
    return [(path, None)]

MAP = mapping()
problems = 0
for f in sorted(pathlib.Path(REPO, "themes").rglob("*.css")):
    rel = str(f.relative_to(REPO))
    now = f.read_text()
    for old_path, block in ancestors(rel):
        before = show(BEFORE, old_path)
        if before is None:
            print(f"-- {rel}{' [' + block + ']' if block else ''}: no pre-port version, skipped")
            continue
        have = declared(now, block)
        missing = {}
        for name in declared(before):
            if name not in MAP:
                continue
            wanted = MAP[name]
            if wanted and not (wanted & have):
                missing[name] = wanted
        if missing:
            problems += 1
            print(f"FAIL {rel}{' [' + block + ']' if block else ''}")
            for name, wanted in sorted(missing.items()):
                print(f"       {name} -> {' or '.join(sorted(wanted))}")
print(f"\n{problems} theme block(s) incomplete." if problems else "\nEvery theme carries all migrated tokens.")
sys.exit(1 if problems else 0)
