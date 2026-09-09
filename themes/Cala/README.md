# Cala

A Balearic palette for JabRef: whitewashed sand and cove water, with pine, terracotta and a little sun. The light scheme puts deep-sea text and cove-blue accents on sand-colored paper, the dark one sand-colored text and turquoise accents on night-sea surfaces. Named after the coves the palette is taken from — Mallorca without the beach bar.

One CSS file covers both color schemes: select it as custom theme and pick _Dark_, _Light_, or _Follow system_ in `File > Preferences > General > Appearance`.

![Dark](cala-dark.png)

![Light](cala-light.png)

## Contrast

Every text/surface pair is checked against WCAG 2 contrast ratios, in both schemes and on every surface (window, tables, toolbar, side pane, search field, tooltips):

| Role                                      | Minimum ratio |
| ----------------------------------------- | ------------- |
| Default text                              | 7:1           |
| Muted text, accent and links as text      | 4.5:1         |
| Text on selection, badges, default button | 4.5:1         |
| Subtle text, status colors as text        | 3:1           |

Cove blue and sun yellow are too light to read as text on sand, so the light scheme uses a darkened cove blue for accent and links and keeps the sun for fills (default button, drag target).
