# Custom JabRef Themes

> Customize the look of JabRef using CSS!

JabRef bundles every theme in this repository that covers both color schemes, its own _JabRef_ theme included; they appear in the theme selection without downloading anything. On top of the theme you can load a custom CSS file that overrides only what you want to change. This page and the [themes](https://github.com/JabRef/themes.jabref.org/tree/main/themes) target the theme model introduced with JabRef 6 ([JabRef/jabref#15798](https://github.com/JabRef/jabref/pull/15798)).

**JabRef 5.x:** the previous versions of the themes, based on the old `-jr-*` variables, are available [in the repository history](https://github.com/JabRef/themes.jabref.org/tree/0a139ff7da4ae356b293f81bd6a38659a7d7fc39/themes).

The [style guide](styleguide.md) states the few rules behind the tokens.

## Themes

All themes, JabRef's own and the contributed ones, are located in the subfolder [themes](https://github.com/JabRef/themes.jabref.org/tree/main/themes). Themes that cover both color schemes in one file (via `@media (prefers-color-scheme: …)`) live directly in `themes/` and work with any color scheme. The _Dark_ and _Light_ subfolders hold the themes that only cover one scheme; select the matching color scheme in JabRef when using those.

## Gallery

All screenshots were taken with JabRef 6 and the theme's CSS file selected as custom theme, on the matching color scheme.

[Dino Girl's themes](https://discourse.jabref.org/t/dino-girls-jabref-themes/3937) pair each dark hue with the light hue closest to it, so one file serves both color schemes. The _blackandwhite_ and _canaryyellow_ hues have no light counterpart and stay dark-only.

### Both color schemes

| Theme                              | Dark                                          | Light                                           |
| ---------------------------------- | --------------------------------------------- | ----------------------------------------------- |
| [Chocolate Honey][chocolate-honey] | ![Chocolate Honey dark][chocolate-honey-dark] | ![Chocolate Honey light][chocolate-honey-light] |
| [Everforest][everforest]           | ![Everforest dark][everforest-dark]           | ![Everforest light][everforest-light]           |
| [JabRef][jabref]                   | ![JabRef dark][jabref-dark]                   | ![JabRef light][jabref-light]                   |
| [Nord][nord]                       | ![Nord dark][nord-dark]                       | ![Nord light][nord-light]                       |
| [Papers][papers]                   | ![Papers dark][papers-dark]                   | ![Papers light][papers-light]                   |
| [Primer][primer]                   | ![Primer dark][primer-dark]                   | ![Primer light][primer-light]                   |

[chocolate-honey]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/ChocolateHoney
[chocolate-honey-dark]: themes/ChocolateHoney/chocolate-honey-dark.png
[chocolate-honey-light]: themes/ChocolateHoney/chocolate-honey-light.png
[everforest]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/Everforest
[everforest-dark]: themes/Everforest/everforest-dark.png
[everforest-light]: themes/Everforest/everforest-light.png
[jabref]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/JabRef
[jabref-dark]: themes/JabRef/jabref-theme-dark.png
[jabref-light]: themes/JabRef/jabref-theme-light.png
[nord]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/Nord
[nord-dark]: themes/Nord/nord-dark.png
[nord-light]: themes/Nord/nord-light.png
[papers]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/Papers
[papers-dark]: themes/Papers/papers-dark.png
[papers-light]: themes/Papers/papers-light.png
[primer]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/Primer
[primer-dark]: themes/Primer/primer-dark.png
[primer-light]: themes/Primer/primer-light.png

#### Dino Girl's themes

| Theme                                                                                  | Dark                                                                                              | Light                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [chocolatebrown-darksalmon-contrasttext][chocolatebrown-darksalmon-contrasttext]       | ![chocolatebrown-darksalmon-contrasttext dark][chocolatebrown-darksalmon-contrasttext-dark]       | ![chocolatebrown-darksalmon-contrasttext light][chocolatebrown-darksalmon-contrasttext-light]       |
| [chocolatebrown-darksalmon-greytext][chocolatebrown-darksalmon-greytext]               | ![chocolatebrown-darksalmon-greytext dark][chocolatebrown-darksalmon-greytext-dark]               | ![chocolatebrown-darksalmon-greytext light][chocolatebrown-darksalmon-greytext-light]               |
| [fuchsiapurple-japanesesakura-contrasttext][fuchsiapurple-japanesesakura-contrasttext] | ![fuchsiapurple-japanesesakura-contrasttext dark][fuchsiapurple-japanesesakura-contrasttext-dark] | ![fuchsiapurple-japanesesakura-contrasttext light][fuchsiapurple-japanesesakura-contrasttext-light] |
| [fuchsiapurple-japanesesakura-greytext][fuchsiapurple-japanesesakura-greytext]         | ![fuchsiapurple-japanesesakura-greytext dark][fuchsiapurple-japanesesakura-greytext-dark]         | ![fuchsiapurple-japanesesakura-greytext light][fuchsiapurple-japanesesakura-greytext-light]         |
| [jabrefdark-jabreflight-contrasttext][jabrefdark-jabreflight-contrasttext]             | ![jabrefdark-jabreflight-contrasttext dark][jabrefdark-jabreflight-contrasttext-dark]             | ![jabrefdark-jabreflight-contrasttext light][jabrefdark-jabreflight-contrasttext-light]             |
| [jabrefdark-jabreflight-greytext][jabrefdark-jabreflight-greytext]                     | ![jabrefdark-jabreflight-greytext dark][jabrefdark-jabreflight-greytext-dark]                     | ![jabrefdark-jabreflight-greytext light][jabrefdark-jabreflight-greytext-light]                     |
| [lightblue-iceage-contrasttext][lightblue-iceage-contrasttext]                         | ![lightblue-iceage-contrasttext dark][lightblue-iceage-contrasttext-dark]                         | ![lightblue-iceage-contrasttext light][lightblue-iceage-contrasttext-light]                         |
| [lightblue-iceage-greytext][lightblue-iceage-greytext]                                 | ![lightblue-iceage-greytext dark][lightblue-iceage-greytext-dark]                                 | ![lightblue-iceage-greytext light][lightblue-iceage-greytext-light]                                 |
| [lightseagreen-limegreen-contrasttext][lightseagreen-limegreen-contrasttext]           | ![lightseagreen-limegreen-contrasttext dark][lightseagreen-limegreen-contrasttext-dark]           | ![lightseagreen-limegreen-contrasttext light][lightseagreen-limegreen-contrasttext-light]           |
| [lightseagreen-limegreen-greytext][lightseagreen-limegreen-greytext]                   | ![lightseagreen-limegreen-greytext dark][lightseagreen-limegreen-greytext-dark]                   | ![lightseagreen-limegreen-greytext light][lightseagreen-limegreen-greytext-light]                   |
| [prehistoricamber-peachorange-contrasttext][prehistoricamber-peachorange-contrasttext] | ![prehistoricamber-peachorange-contrasttext dark][prehistoricamber-peachorange-contrasttext-dark] | ![prehistoricamber-peachorange-contrasttext light][prehistoricamber-peachorange-contrasttext-light] |
| [prehistoricamber-peachorange-greytext][prehistoricamber-peachorange-greytext]         | ![prehistoricamber-peachorange-greytext dark][prehistoricamber-peachorange-greytext-dark]         | ![prehistoricamber-peachorange-greytext light][prehistoricamber-peachorange-greytext-light]         |
| [twilightlavender-neon-contrasttext][twilightlavender-neon-contrasttext]               | ![twilightlavender-neon-contrasttext dark][twilightlavender-neon-contrasttext-dark]               | ![twilightlavender-neon-contrasttext light][twilightlavender-neon-contrasttext-light]               |
| [twilightlavender-neon-greytext][twilightlavender-neon-greytext]                       | ![twilightlavender-neon-greytext dark][twilightlavender-neon-greytext-dark]                       | ![twilightlavender-neon-greytext light][twilightlavender-neon-greytext-light]                       |
| [winered-icedstrawberry-contrasttext][winered-icedstrawberry-contrasttext]             | ![winered-icedstrawberry-contrasttext dark][winered-icedstrawberry-contrasttext-dark]             | ![winered-icedstrawberry-contrasttext light][winered-icedstrawberry-contrasttext-light]             |
| [winered-icedstrawberry-greytext][winered-icedstrawberry-greytext]                     | ![winered-icedstrawberry-greytext dark][winered-icedstrawberry-greytext-dark]                     | ![winered-icedstrawberry-greytext light][winered-icedstrawberry-greytext-light]                     |

[chocolatebrown-darksalmon-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext.css
[chocolatebrown-darksalmon-contrasttext-dark]: themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext-dark.png
[chocolatebrown-darksalmon-contrasttext-light]: themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext-light.png
[chocolatebrown-darksalmon-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext.css
[chocolatebrown-darksalmon-greytext-dark]: themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext-dark.png
[chocolatebrown-darksalmon-greytext-light]: themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext-light.png
[fuchsiapurple-japanesesakura-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext.css
[fuchsiapurple-japanesesakura-contrasttext-dark]: themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext-dark.png
[fuchsiapurple-japanesesakura-contrasttext-light]: themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext-light.png
[fuchsiapurple-japanesesakura-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext.css
[fuchsiapurple-japanesesakura-greytext-dark]: themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext-dark.png
[fuchsiapurple-japanesesakura-greytext-light]: themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext-light.png
[jabrefdark-jabreflight-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext.css
[jabrefdark-jabreflight-contrasttext-dark]: themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext-dark.png
[jabrefdark-jabreflight-contrasttext-light]: themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext-light.png
[jabrefdark-jabreflight-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext.css
[jabrefdark-jabreflight-greytext-dark]: themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext-dark.png
[jabrefdark-jabreflight-greytext-light]: themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext-light.png
[lightblue-iceage-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightblue-iceage-contrasttext.css
[lightblue-iceage-contrasttext-dark]: themes/DinoGirls%20Themes/lightblue-iceage-contrasttext-dark.png
[lightblue-iceage-contrasttext-light]: themes/DinoGirls%20Themes/lightblue-iceage-contrasttext-light.png
[lightblue-iceage-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightblue-iceage-greytext.css
[lightblue-iceage-greytext-dark]: themes/DinoGirls%20Themes/lightblue-iceage-greytext-dark.png
[lightblue-iceage-greytext-light]: themes/DinoGirls%20Themes/lightblue-iceage-greytext-light.png
[lightseagreen-limegreen-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext.css
[lightseagreen-limegreen-contrasttext-dark]: themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext-dark.png
[lightseagreen-limegreen-contrasttext-light]: themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext-light.png
[lightseagreen-limegreen-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext.css
[lightseagreen-limegreen-greytext-dark]: themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext-dark.png
[lightseagreen-limegreen-greytext-light]: themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext-light.png
[prehistoricamber-peachorange-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext.css
[prehistoricamber-peachorange-contrasttext-dark]: themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext-dark.png
[prehistoricamber-peachorange-contrasttext-light]: themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext-light.png
[prehistoricamber-peachorange-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext.css
[prehistoricamber-peachorange-greytext-dark]: themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext-dark.png
[prehistoricamber-peachorange-greytext-light]: themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext-light.png
[twilightlavender-neon-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext.css
[twilightlavender-neon-contrasttext-dark]: themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext-dark.png
[twilightlavender-neon-contrasttext-light]: themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext-light.png
[twilightlavender-neon-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/twilightlavender-neon-greytext.css
[twilightlavender-neon-greytext-dark]: themes/DinoGirls%20Themes/twilightlavender-neon-greytext-dark.png
[twilightlavender-neon-greytext-light]: themes/DinoGirls%20Themes/twilightlavender-neon-greytext-light.png
[winered-icedstrawberry-contrasttext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext.css
[winered-icedstrawberry-contrasttext-dark]: themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext-dark.png
[winered-icedstrawberry-contrasttext-light]: themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext-light.png
[winered-icedstrawberry-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/winered-icedstrawberry-greytext.css
[winered-icedstrawberry-greytext-dark]: themes/DinoGirls%20Themes/winered-icedstrawberry-greytext-dark.png
[winered-icedstrawberry-greytext-light]: themes/DinoGirls%20Themes/winered-icedstrawberry-greytext-light.png

### Dark themes

| Theme                                                                                              | Preview                                                                           |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [DARK THEME-blackandwhite-greytext][dark-theme-blackandwhite-greytext] (Dino Girl's dark themes)   | ![DARK THEME-blackandwhite-greytext][dark-theme-blackandwhite-greytext-preview]   |
| [DARK THEME-blackandwhite-whitetext][dark-theme-blackandwhite-whitetext] (Dino Girl's dark themes) | ![DARK THEME-blackandwhite-whitetext][dark-theme-blackandwhite-whitetext-preview] |
| [DARK THEME-canaryyellow-greytext][dark-theme-canaryyellow-greytext] (Dino Girl's dark themes)     | ![DARK THEME-canaryyellow-greytext][dark-theme-canaryyellow-greytext-preview]     |
| [Dracula][dracula]                                                                                 | ![Dracula][dracula-preview]                                                       |
| [GnomeDarkOrange][gnomedarkorange]                                                                 | ![GnomeDarkOrange][gnomedarkorange-preview]                                       |
| [JabRef-black][jabref-black]                                                                       | ![JabRef-black][jabref-black-preview]                                             |

[dark-theme-blackandwhite-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-greytext.css
[dark-theme-blackandwhite-greytext-preview]: themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-greytext.png
[dark-theme-blackandwhite-whitetext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-whitetext.css
[dark-theme-blackandwhite-whitetext-preview]: themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-whitetext.png
[dark-theme-canaryyellow-greytext]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-canaryyellow-greytext.css
[dark-theme-canaryyellow-greytext-preview]: themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-canaryyellow-greytext.png
[dracula]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/Dracula
[dracula-preview]: themes/DarkTheme/Dracula/screenshots/preview.png
[gnomedarkorange]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/GnomeDarkOrange
[gnomedarkorange-preview]: themes/DarkTheme/GnomeDarkOrange/jabref_gnome_dark_orange.png
[jabref-black]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/JabRef-black
[jabref-black-preview]: themes/DarkTheme/JabRef-black/preview.png

### Light themes

| Theme                    | Preview                           |
| ------------------------ | --------------------------------- |
| [Interoctiv][interoctiv] | ![Interoctiv][interoctiv-preview] |

[interoctiv]: https://github.com/JabRef/themes.jabref.org/blob/main/themes/LightTheme/Interoctiv
[interoctiv-preview]: themes/LightTheme/Interoctiv/wrap-text.png

## Use a custom theme

1. Open `File > Preferences > General`.
2. In the _Appearance_ section, choose a _Theme_ and a _Color scheme_ (_Follow system_, _Light_, or _Dark_).
3. Tick _Custom theme_ and select your CSS file.

The custom CSS is applied on top of the selected theme and color scheme. Changes to the file are picked up while JabRef is running, so you can edit it and watch the result.

## Creating a new theme

All colors of a theme are `-color-*` variables, for example `-color-accent`, `-color-bg-primary`, `-color-fg-default`, or `-color-selection`. The complete list, with a comment on what each one is used for, is in [`jabref-theme.css`](themes/JabRef/jabref-theme.css) (and [`primer.css`](themes/Primer/primer.css) for the second theme). The rest of JabRef's styling only uses these variables, so overriding them is all that is needed to re-color the whole UI.

Override a variable for both color schemes:

```css
.root {
    -color-accent: #8F0D11;
}
```

Override it for one color scheme only. The media query follows the color scheme selected in JabRef (or the operating system, with _Follow system_):

```css
@media (prefers-color-scheme: dark) {
    .root {
        -color-accent: #ff79c6;
    }
}
```

Anything else (fonts, sizes, individual controls) can be styled with regular JavaFX CSS; [`jabref-base.css`](https://github.com/JabRef/jabref/blob/main/jabgui/src/main/resources/org/jabref/gui/theme/internal/jabref-base.css) shows the style classes JabRef uses.

### Migrating a theme from JabRef 5.x

The old `-jr-*` variables no longer exist and are silently ignored. Every variable the previous themes set maps as follows:

| JabRef 5.x                                                            | JabRef 6                                                       |
| --------------------------------------------------------------------- | -------------------------------------------------------------- |
| `-jr-theme`                                                           | `-color-accent`, `-color-link`                                 |
| `-jr-accent`                                                          | `-color-accent-subtle`, `-color-selection`                     |
| `-jr-hover`                                                           | `-color-overlay-hover`, `-color-button-hover`                  |
| `-jr-base`, `-jr-menu-background`, `-jr-toolbar`                      | `-color-bg-tertiary`                                           |
| `-jr-background-alt`                                                  | `-color-bg-primary`                                            |
| `-jr-row-odd-background` / `-jr-row-even-background`                  | `-color-bg-secondary` / `-color-bg-alt`                        |
| `-jr-search-background`                                               | `-color-bg-search`                                             |
| `-jr-sidepane-background`                                             | `-color-bg-sidepane`                                           |
| `-jr-separator`                                                       | `-color-border-light`                                          |
| `-fx-light-text-color` / `-fx-dark-text-color` / `-fx-mid-text-color` | `-color-fg-emphasis` / `-color-fg-default` / `-color-fg-muted` |
| `-fx-control-inner-background` / `-fx-control-inner-background-alt`   | `-color-bg-secondary` / `-color-bg-alt`                        |
| `-fx-outer-border`                                                    | `-color-border-light`, `-color-button-border`                  |
| `-fx-focused-text-base-color`                                         | `-color-fg-emphasis`                                           |
| `-jr-green` / `-jr-light-green`                                       | `-color-success` / `-color-success-emphasis`                   |
| `-jr-orange`                                                          | `-color-warning`                                               |
| `-jr-light-red` / `-jr-red`                                           | `-color-danger` / `-color-danger-emphasis`                     |
| `-jr-scrollbar-thumb` / `-jr-scrollbar-track`                         | `-color-scrollbar-thumb` / `-color-scrollbar-track`            |
| `-jr-tooltip-bg` / `-jr-tooltip-fg`                                   | `-color-tooltip-bg` / `-color-fg-default`                      |
| `-jr-drag-target` / `-jr-drag-target-hover`                           | `-color-drag-target` / `-color-drag-target-hover`              |
| `-jr-group-hits-bg` / `-jr-group-hits-fg`                             | `-color-badge-bg` / `-color-fg-emphasis`                       |
| `-jr-selected`                                                        | `-color-selection`                                             |
| `-jr-accent-alt` / `-jr-transparent-accent`                           | `-color-accent-subtle` / `-color-selection-inactive`           |
| `-jr-checked`                                                         | `-color-accent`                                                |
| `-jr-text-area-background`                                            | `-color-bg-search`                                             |
| `-jr-sidepane-header-background`                                      | `-color-bg-sidepane`                                           |
| `-jr-icon` / `-jr-icon-active`                                        | `-color-fg-default` / `-color-accent`                          |
| `-jr-icon-background`                                                 | `-color-button`                                                |
| `-jr-icon-background-active`, `-jr-menu-background-active`            | `-color-overlay-hover`                                         |
| `-jr-icon-background-armed`                                           | `-color-overlay-armed`                                         |
| `-jr-warn` / `-jr-error` / `-jr-info`                                 | `-color-warning` / `-color-danger` / `-color-info`             |

In a dark theme the readable body color is the old `-fx-light-text-color`, so give `-color-fg-default` that value as well.

Three groups do not fit a cell:

* `-jr-theme-text`, `-jr-search-text`, `-jr-head-fg`, `-jr-sidepane-header-color`, `-jr-menu-foreground`, `-jr-menu-item-foreground` and `-jr-menu-forground-active` all become `-color-fg-default`, or `-color-fg-emphasis` where the text sits on an accent-colored surface.
* `-jr-white`, `-jr-black`, `-jr-blue`, `-jr-light-blue`, `-jr-purple`, `-jr-light-purple`, `-jr-yellow`, `-jr-gray-0` to `-jr-gray-3` and `-jr-blue-gray-1` to `-jr-blue-gray-4` are raw palette entries with no successor. Set the token of the element you colored with them.
* `-jr-header-height` is not a color. Style the element directly, for example with `-fx-pref-height`.

Old themes were complete copies of JabRef's stylesheet. That is no longer needed: keep only the variables you change.

## Selection of Useful CSS selectors

| UI element                       | CSS selector       |
| -------------------------------- | ------------------ |
| preview box                      | `#previewBody`     |
| `{} biblatex source` tab         | `.code-area`       |
| text in `{} biblatex source` tab | `.code-area .text` |

