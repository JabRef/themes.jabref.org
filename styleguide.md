# Style guide

Short rules behind the JabRef theme; the CSS carries no reasoning.

## Borders

- `-color-border-light`: the frame of buttons, text fields and surfaces.
- `-color-border-strong`: the check box square only. The 2px frame *is* the control, so it has to read on its own.
- `-color-border-muted`: separators and dividers.
- Tabs draw no frame. The selected tab is marked by its accent line and background, hovering tints the others (Firefox, IntelliJ).

Separate tokens for separate purposes, at the price of one more line per theme.

## Icons

One color. An icon takes the color of the text next to it; no color coding by kind.

## Foregrounds

A color that a theme picks as a *fill* must never be used as a foreground. `-color-selection`,
`-color-accent-subtle`, `-color-badge-bg`, `-color-drag-target` and `-color-scrollbar-thumb` are
fills, so the themes tune them for text drawn *on* them, not for reading against a surface. Text
and icons take `-color-fg-*`, `-color-accent` or `-color-link`, whose contrast every theme states in its own
contract.

## Contrast

Text is readable on every surface it can appear on. The floor is WCAG 2: 4.5:1 for anything a
reader spells out, 3:1 where a color only has to be distinguishable. A theme may aim higher in
its README, and most do.

`check-contrast.py` measures every palette against that floor, layering a theme that only
overrides tokens on top of the JabRef theme the way JabRef does at runtime.
`contrast-baseline.txt` records how much each theme still carries, so a theme can only get
better and a new one starts clean.
