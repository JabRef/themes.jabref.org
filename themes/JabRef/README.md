# JabRef

JabRef's default look. One CSS file covers both color schemes; JabRef bundles it from this repository and selects it when no other theme is chosen.

![Dark](jabref-theme-dark.png)

![Light](jabref-theme-light.png)

This file declares the complete `-color-*` token contract and styles the JavaFX controls with it. Every other theme here except Primer is layered on top of it and overrides only the tokens it changes, so a token added or removed here changes what those themes can override.
