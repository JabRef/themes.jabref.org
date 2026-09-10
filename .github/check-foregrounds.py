"""Enforce the "Foregrounds" rule of the style guide: a token a theme tunes as a *fill*
is tuned for text drawn on it, so it must never be the color of the text itself. The
list of fill tokens is read from styleguide.md so the check cannot drift from the rule."""
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

# Properties that paint text or an icon onto whatever surface is behind it.
# -fx-highlight-text-fill is left out: that text sits on a fill, not on the surface.
FOREGROUND = re.compile(r"^\s*(-fx-(?:text-fill|fill|prompt-text-fill|icon-color|mark-color))\s*:([^;]*);", re.M)

# Line wrapping is not part of the rule, so the sentence is read as one line.
guide = " ".join(pathlib.Path(REPO, "styleguide.md").read_text().split())
sentence = re.search(r"## Foregrounds.*?(`-color-.*?) are fills", guide)
if not sentence:
    sys.exit("styleguide.md names no fill tokens; has the Foregrounds section moved?")
fills = set(re.findall(r"`(-color-[a-z0-9-]+)`", sentence.group(1)))

problems = 0
for css in sorted(pathlib.Path(REPO, "themes").rglob("*.css")):
    text = re.sub(r"(?s)/\*.*?\*/", " ", css.read_text())
    for match in FOREGROUND.finditer(text):
        used = fills.intersection(re.findall(r"-color-[a-z0-9-]+", match.group(2)))
        if used:
            problems += 1
            line = text.count("\n", 0, match.start()) + 1
            print(f"FAIL {css.relative_to(REPO)}:{line}  {match.group(1)}: {' '.join(sorted(used))}")

print(f"\n{problems} foreground(s) painted in a fill token." if problems
      else f"\nNo foreground uses one of the {len(fills)} fill tokens.")
sys.exit(1 if problems else 0)
