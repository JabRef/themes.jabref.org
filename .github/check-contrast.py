"""Measure every theme's palette against the contrast floor of the style guide: text has to be
readable on each surface it can appear on, and the few foregrounds that are drawn on a fill have
to be readable on that fill.

A theme that only overrides tokens is measured on top of the JabRef theme, the way JabRef layers
it at runtime. contrast-baseline.txt says how much each theme still carries, so the check stops
new shortfalls instead of demanding that every theme be fixed at once.
"""
import hashlib
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
BASELINE = pathlib.Path(__file__).with_name("contrast-baseline.txt")
BASE_THEME = REPO / "themes" / "JabRef" / "jabref-theme.css"

# Where a foreground can actually appear. Body text lands on every surface; links and status
# colors on the surfaces that carry content; syntax colors only in the source editor and the
# search field. A tooltip carries -color-fg-default only, hence its narrow entry.
EVERYWHERE = ["-color-bg-primary", "-color-bg-secondary", "-color-bg-tertiary", "-color-bg-alt",
              "-color-bg-search", "-color-bg-sidepane", "-color-bg-overlay", "-color-tooltip-bg"]
CONTENT = ["-color-bg-primary", "-color-bg-secondary", "-color-bg-tertiary", "-color-bg-alt",
           "-color-bg-sidepane", "-color-bg-overlay"]
EDITOR = ["-color-bg-secondary", "-color-bg-search"]

# Text on a surface, at the WCAG 2 minimum for that kind of text: 4.5:1 for body text and
# for anything a reader has to spell out, 3:1 where the color only has to be distinguishable.
# The themes aim higher in their own contracts; CI holds the floor.
ON_SURFACE = {"-color-fg-default": (4.5, EVERYWHERE), "-color-fg-muted": (4.5, EVERYWHERE),
              "-color-fg-subtle": (3.0, EVERYWHERE),
              "-color-accent": (4.5, CONTENT), "-color-link": (4.5, CONTENT),
              "-color-link-hover": (4.5, CONTENT),
              "-color-success": (3.0, CONTENT), "-color-warning": (3.0, CONTENT),
              "-color-danger": (3.0, CONTENT),
              "-color-syntax-keyword": (4.5, EDITOR), "-color-syntax-tag": (4.5, EDITOR),
              "-color-syntax-attribute": (4.5, EDITOR), "-color-syntax-string": (4.5, EDITOR),
              "-color-syntax-comment": (3.0, EDITOR), "-color-syntax-punctuation": (4.5, EDITOR)}

# Text on a fill. A group that is only partly selected gets a much paler green than
# -color-success, and a selected icon button is the emphasis color on the hover overlay, which
# is translucent -- such a fill is measured over each surface it can lie on.
ON_FILL = {"-color-fg-emphasis": ["-color-selection", "-color-badge-bg", "-color-button-default",
                                  "-color-overlay-hover"],
           "-color-badge-selected-fg": ["-color-success", "derive(-color-success, 70%)"]}

NAMED = {"white": (255, 255, 255), "black": (0, 0, 0)}


def luminance(color):
    def channel(value):
        value /= 255
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4
    red, green, blue = (channel(part) for part in color)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def ratio(foreground, background):
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def color(value, tokens, backdrop=None, depth=0):
    """The value as RGB, or None for anything a ratio cannot be computed from. Token references
    and derive() are followed, so a theme cannot hide a shortfall behind an indirection. A
    translucent color needs a backdrop to lie on; without one it has no ratio of its own."""
    value = value.strip()
    if depth > 10:
        return None
    if value in NAMED:
        return NAMED[value]
    if value in tokens:
        return color(tokens[value], tokens, backdrop, depth + 1)
    hex_color = re.fullmatch(r"#([0-9a-fA-F]{3,8})", value)
    if hex_color:
        digits = hex_color.group(1)
        if len(digits) in (3, 4):
            digits = "".join(digit * 2 for digit in digits)
        parts = [int(digits[index:index + 2], 16) for index in range(0, len(digits), 2)]
        return blend(parts[:3], parts[3] / 255 if len(parts) == 4 else 1.0, backdrop)
    translucent = re.fullmatch(r"rgba?\(([^)]*)\)", value)
    if translucent:
        parts = [part.strip() for part in translucent.group(1).split(",")]
        return blend([int(part) for part in parts[:3]],
                     float(parts[3]) if len(parts) == 4 else 1.0, backdrop)
    derived = re.fullmatch(r"derive\(\s*(.+?)\s*,\s*(-?[0-9.]+)%\s*\)", value)
    if derived:
        base = color(derived.group(1), tokens, backdrop, depth + 1)
        return derive(base, float(derived.group(2))) if base else None
    return None


def blend(rgb, alpha, backdrop):
    """The color as it is seen: opaque colors as they are, translucent ones over the backdrop."""
    if alpha >= 1:
        return tuple(rgb)
    if backdrop is None:
        return None
    return tuple(round(alpha * part + (1 - alpha) * behind) for part, behind in zip(rgb, backdrop))


def derive(rgb, percent):
    """JavaFX's derive(): the HSB brightness is scaled by the percentage, towards black for a
    negative one and towards white for a positive one."""
    factor = 1 + percent / 100
    brightness = max(rgb) / 255
    if factor <= 1:
        target = brightness * factor
    else:
        target = brightness + (1 - brightness) * (factor - 1)
    scale = target / brightness if brightness else 0
    return tuple(min(255, round(part * scale)) if brightness else round(255 * target)
                 for part in rgb)


def palettes(css):
    """The theme's tokens per color scheme. A declaration outside a media query counts for
    both schemes, which is how a single-scheme theme and Primer declare theirs."""
    text = re.sub(r"(?s)/\*.*?\*/", " ", css.read_text())
    schemes = {}
    for scheme in ("light", "dark"):
        blocks = re.findall(r"prefers-color-scheme:\s*" + scheme + r"\s*\)\s*\{(.*?\n\s*\})\s*\}",
                            text, re.S)
        shared = re.sub(r"(?s)@media.*?\n\}", " ", text)
        tokens = {}
        for block in [shared] + blocks:
            tokens.update(re.findall(r"(-color-[a-z0-9-]+)\s*:\s*([^;]+);", block))
        schemes[scheme] = tokens
    return schemes


def failures(theme, base):
    for scheme in ("light", "dark"):
        tokens = dict(base[scheme])
        tokens.update(theme[scheme])
        resolved = {name: color(value, tokens) for name, value in tokens.items()}
        pairs = [(fg, bg, resolved.get(bg), target)
                 for fg, (target, surfaces) in ON_SURFACE.items() for bg in surfaces]
        for foreground, fills in ON_FILL.items():
            for fill in fills:
                if color(fill, tokens):
                    pairs.append((foreground, fill, color(fill, tokens), 4.5))
                    continue
                # Translucent: what shows through decides, so measure it on each surface.
                for surface in EVERYWHERE:
                    over = color(fill, tokens, resolved.get(surface))
                    pairs.append((foreground, f"{fill} over {surface}", over, 4.5))
        for foreground, background, behind, target in pairs:
            if resolved.get(foreground) and behind:
                measured = ratio(resolved[foreground], behind)
                if measured < target:
                    yield scheme, foreground, background, measured, target


base_palette = palettes(BASE_THEME)

# How many shortfalls a theme still carries, and a fingerprint of which ones they are: swapping
# one shortfall for another keeps the count and has to be caught as well. A theme that is not
# listed has to have none, so a new theme starts clean and an existing one can only get better.
allowed = {}
for line in BASELINE.read_text().splitlines():
    line = line.split("#")[0].strip()
    if line:
        theme, count, fingerprint = line.rsplit(" ", 2)
        allowed[theme] = (int(count), fingerprint)

worse, better, measured_themes = [], [], set()
# The DarkTheme/ and LightTheme/ folders hold the themes that were never ported to the token
# contract; the migration audit covers those.
for css in sorted(pathlib.Path(REPO, "themes").glob("*/*.css")):
    theme = css.relative_to(REPO / "themes").with_suffix("").as_posix()
    measured_themes.add(theme)
    found = list(failures(palettes(css), base_palette))
    for scheme, foreground, background, measured, target in found:
        print(f"  {theme} {scheme}: {foreground} on {background} {measured:.2f} < {target}")
    pairs = sorted(f"{scheme} {foreground} {background}" for scheme, foreground, background, _, _ in found)
    fingerprint = hashlib.sha1(" ".join(pairs).encode()).hexdigest()[:8]
    count, baselined = allowed.get(theme, (0, fingerprint))
    if len(found) > count:
        worse.append(f"{theme}: {len(found)} shortfall(s), {count} allowed")
    elif len(found) < count:
        better.append(f"{theme}: {len(found)} shortfall(s) left, write "
                      f"\"{theme} {len(found)} {fingerprint}\" into contrast-baseline.txt")
    elif fingerprint != baselined:
        worse.append(f"{theme}: same number of shortfalls, but other ones -- see the list above; "
                     f"if that is intended, write \"{theme} {len(found)} {fingerprint}\"")

print()
for line in worse:
    print("FAIL " + line)
for line in better:
    print("note " + line)
for theme in sorted(allowed.keys() - measured_themes):
    print(f"note {theme} is baselined but no longer exists; drop the line")

print(f"\n{len(worse)} theme(s) below the contrast floor." if worse
      else "\nNo theme is worse than its baseline.")
sys.exit(1 if worse else 0)
