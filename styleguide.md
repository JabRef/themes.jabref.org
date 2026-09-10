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
