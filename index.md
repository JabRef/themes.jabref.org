# Custom JabRef Themes

> Customize the look of JabRef using CSS!

JabRef ships two themes, _JabRef_ and _Primer_, each with a light and a dark variant. On top of the theme you can load a custom CSS file that overrides only what you want to change. This page and the [user contributed themes](https://github.com/JabRef/themes.jabref.org/tree/main/themes) target the theme model introduced with JabRef 6 ([JabRef/jabref#15798](https://github.com/JabRef/jabref/pull/15798)).

**JabRef 5.x:** the previous versions of the themes, based on the old `-jr-*` variables, are available [in the repository history](https://github.com/JabRef/themes.jabref.org/tree/0a139ff7da4ae356b293f81bd6a38659a7d7fc39/themes).

## User contributed themes

Themes submitted by users are located in the subfolder [themes](https://github.com/JabRef/themes.jabref.org/tree/main/themes). Themes that cover both color schemes in one file (via `@media (prefers-color-scheme: …)`) live directly in `themes/` and work with any color scheme. The _Dark_ and _Light_ subfolders hold the themes that only cover one scheme; select the matching color scheme in JabRef when using those.

## Gallery

All screenshots were taken with JabRef 6 and the theme's CSS file selected as custom theme, on the matching color scheme.

The DinoGirls collection pairs each dark hue with the light hue closest to it, so one file serves both color schemes. The _blackandwhite_ and _canaryyellow_ hues have no light counterpart and stay dark-only.

### Both color schemes

| Theme | Dark | Light |
| --- | --- | --- |
| [Everforest](https://github.com/JabRef/themes.jabref.org/blob/main/themes/Everforest) | ![Everforest dark](themes/Everforest/everforest-dark.png) | ![Everforest light](themes/Everforest/everforest-light.png) |
| [chocolatebrown-darksalmon-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext.css) (DinoGirls Themes) | ![chocolatebrown-darksalmon-contrasttext dark](themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext-dark.png) | ![chocolatebrown-darksalmon-contrasttext light](themes/DinoGirls%20Themes/chocolatebrown-darksalmon-contrasttext-light.png) |
| [chocolatebrown-darksalmon-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext.css) (DinoGirls Themes) | ![chocolatebrown-darksalmon-greytext dark](themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext-dark.png) | ![chocolatebrown-darksalmon-greytext light](themes/DinoGirls%20Themes/chocolatebrown-darksalmon-greytext-light.png) |
| [fuchsiapurple-japanesesakura-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext.css) (DinoGirls Themes) | ![fuchsiapurple-japanesesakura-contrasttext dark](themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext-dark.png) | ![fuchsiapurple-japanesesakura-contrasttext light](themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-contrasttext-light.png) |
| [fuchsiapurple-japanesesakura-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext.css) (DinoGirls Themes) | ![fuchsiapurple-japanesesakura-greytext dark](themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext-dark.png) | ![fuchsiapurple-japanesesakura-greytext light](themes/DinoGirls%20Themes/fuchsiapurple-japanesesakura-greytext-light.png) |
| [jabrefdark-jabreflight-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext.css) (DinoGirls Themes) | ![jabrefdark-jabreflight-contrasttext dark](themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext-dark.png) | ![jabrefdark-jabreflight-contrasttext light](themes/DinoGirls%20Themes/jabrefdark-jabreflight-contrasttext-light.png) |
| [jabrefdark-jabreflight-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext.css) (DinoGirls Themes) | ![jabrefdark-jabreflight-greytext dark](themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext-dark.png) | ![jabrefdark-jabreflight-greytext light](themes/DinoGirls%20Themes/jabrefdark-jabreflight-greytext-light.png) |
| [lightblue-iceage-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightblue-iceage-contrasttext.css) (DinoGirls Themes) | ![lightblue-iceage-contrasttext dark](themes/DinoGirls%20Themes/lightblue-iceage-contrasttext-dark.png) | ![lightblue-iceage-contrasttext light](themes/DinoGirls%20Themes/lightblue-iceage-contrasttext-light.png) |
| [lightblue-iceage-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightblue-iceage-greytext.css) (DinoGirls Themes) | ![lightblue-iceage-greytext dark](themes/DinoGirls%20Themes/lightblue-iceage-greytext-dark.png) | ![lightblue-iceage-greytext light](themes/DinoGirls%20Themes/lightblue-iceage-greytext-light.png) |
| [lightseagreen-limegreen-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext.css) (DinoGirls Themes) | ![lightseagreen-limegreen-contrasttext dark](themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext-dark.png) | ![lightseagreen-limegreen-contrasttext light](themes/DinoGirls%20Themes/lightseagreen-limegreen-contrasttext-light.png) |
| [lightseagreen-limegreen-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext.css) (DinoGirls Themes) | ![lightseagreen-limegreen-greytext dark](themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext-dark.png) | ![lightseagreen-limegreen-greytext light](themes/DinoGirls%20Themes/lightseagreen-limegreen-greytext-light.png) |
| [prehistoricamber-peachorange-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext.css) (DinoGirls Themes) | ![prehistoricamber-peachorange-contrasttext dark](themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext-dark.png) | ![prehistoricamber-peachorange-contrasttext light](themes/DinoGirls%20Themes/prehistoricamber-peachorange-contrasttext-light.png) |
| [prehistoricamber-peachorange-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext.css) (DinoGirls Themes) | ![prehistoricamber-peachorange-greytext dark](themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext-dark.png) | ![prehistoricamber-peachorange-greytext light](themes/DinoGirls%20Themes/prehistoricamber-peachorange-greytext-light.png) |
| [twilightlavender-neon-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext.css) (DinoGirls Themes) | ![twilightlavender-neon-contrasttext dark](themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext-dark.png) | ![twilightlavender-neon-contrasttext light](themes/DinoGirls%20Themes/twilightlavender-neon-contrasttext-light.png) |
| [twilightlavender-neon-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/twilightlavender-neon-greytext.css) (DinoGirls Themes) | ![twilightlavender-neon-greytext dark](themes/DinoGirls%20Themes/twilightlavender-neon-greytext-dark.png) | ![twilightlavender-neon-greytext light](themes/DinoGirls%20Themes/twilightlavender-neon-greytext-light.png) |
| [winered-icedstrawberry-contrasttext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext.css) (DinoGirls Themes) | ![winered-icedstrawberry-contrasttext dark](themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext-dark.png) | ![winered-icedstrawberry-contrasttext light](themes/DinoGirls%20Themes/winered-icedstrawberry-contrasttext-light.png) |
| [winered-icedstrawberry-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DinoGirls%20Themes/winered-icedstrawberry-greytext.css) (DinoGirls Themes) | ![winered-icedstrawberry-greytext dark](themes/DinoGirls%20Themes/winered-icedstrawberry-greytext-dark.png) | ![winered-icedstrawberry-greytext light](themes/DinoGirls%20Themes/winered-icedstrawberry-greytext-light.png) |

### Dark themes

| Theme | Preview |
| --- | --- |
| [DARK THEME-blackandwhite-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-greytext.css) (DinoGirls Dark Themes) | ![DARK THEME-blackandwhite-greytext](themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-greytext.png) |
| [DARK THEME-blackandwhite-whitetext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-whitetext.css) (DinoGirls Dark Themes) | ![DARK THEME-blackandwhite-whitetext](themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-blackandwhite-whitetext.png) |
| [DARK THEME-canaryyellow-greytext](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-canaryyellow-greytext.css) (DinoGirls Dark Themes) | ![DARK THEME-canaryyellow-greytext](themes/DarkTheme/DinoGirls%20Dark%20Themes/DARK%20THEME-canaryyellow-greytext.png) |
| [Dracula](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/Dracula) | ![Dracula](themes/DarkTheme/Dracula/screenshots/preview.png) |
| [GnomeDarkOrange](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/GnomeDarkOrange) | ![GnomeDarkOrange](themes/DarkTheme/GnomeDarkOrange/jabref_gnome_dark_orange.png) |
| [JabRef-black](https://github.com/JabRef/themes.jabref.org/blob/main/themes/DarkTheme/JabRef-black) | ![JabRef-black](themes/DarkTheme/JabRef-black/preview.png) |

### Light themes

| Theme | Preview |
| --- | --- |
| [Interoctiv](https://github.com/JabRef/themes.jabref.org/blob/main/themes/LightTheme/Interoctiv) | ![Interoctiv](themes/LightTheme/Interoctiv/wrap-text.png) |

## Use a custom theme

1. Open `File > Preferences > General`.
2. In the _Appearance_ section, choose a _Theme_ and a _Color scheme_ (_Follow system_, _Light_, or _Dark_).
3. Tick _Custom theme_ and select your CSS file.

The custom CSS is applied on top of the selected theme and color scheme. Changes to the file are picked up while JabRef is running, so you can edit it and watch the result.

## Creating a new theme

All colors of a theme are `-color-*` variables, for example `-color-accent`, `-color-bg-primary`, `-color-fg-default`, or `-color-selection`. The complete list, with a comment on what each one is used for, is in [`jabref-theme.css`](https://github.com/JabRef/jabref/blob/main/jabgui/src/main/resources/org/jabref/gui/theme/jabref-theme.css) (and [`primer-theme.css`](https://github.com/JabRef/jabref/blob/main/jabgui/src/main/resources/org/jabref/gui/theme/primer-theme.css) for the second theme). The rest of JabRef's styling only uses these variables, so overriding them is all that is needed to re-color the whole UI.

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
| `-jr-separator`                                                       | `-color-border-default`                                        |
| `-fx-light-text-color` / `-fx-dark-text-color` / `-fx-mid-text-color` | `-color-fg-emphasis` / `-color-fg-default` / `-color-fg-muted` |
| `-fx-control-inner-background` / `-fx-control-inner-background-alt`   | `-color-bg-secondary` / `-color-bg-alt`                        |
| `-fx-outer-border`                                                    | `-color-border-default`, `-color-button-border`                |
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

## Known bugs

* [#8523](https://github.com/JabRef/jabref/issues/8523): On Windows 10, it is not possible to use fonts that were installed user-wide in the CSS, only system-wide fonts are working. A workaround to use fonts that are not installed system-wide is to include the font file via [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face).
