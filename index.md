# Custom Themes

> Customize the look of JabRef using CSS!

The look of JabRef 5.1 and later can be customized by importing custom CSS files. Imported themes, as well as the two basic themes _Light_ and _Dark_, can be exported from JabRef in the form of CSS files. [Light Theme](https://github.com/JabRef/jabref/blob/main/src/main/java/org/jabref/gui/Base.css) and [Dark Theme](https://github.com/JabRef/jabref/blob/main/src/main/java/org/jabref/gui/Dark.css)

## User contributed themes

Themes submitted by users are located in the subfolder [themes](themes/) and are either _Dark_ themes or _Light_ themes

## Import CSS file

### Jabref version >= 5.10

To import a CSS file to JabRef click File -> Preferences
In the General tab select _Custom_ and select the CSS file.

![Alt text](preferences-general-5.10.png)

Keep in mind that the changes will not take effect until you have restarted JabRef.

### JabRef version < 5.10

To import a CSS file to JabRef click on Options -> Preferences (in newer JabRef versions File -> Preferences), then on the _Import theme_ button in the lower-left corner. Now navigate to your CSS file using the opened dialog box, select your file and click _open_.

After the dialog box has closed, go to the _Appearance_ tab (use the search box if you can't find it) in preferences and under _Visual theme_ chose the _Custom theme_ option. Then click _Save_ in the lower-right corner and restart the JabRef.

Keep in mind that the changes will not take effect until you have restarted JabRef.

![Custom theme toggled](custom-theme-toggled.png)

## Export an existing theme

To export a theme click on _Options_ -> _Preferences_,  then on the _Export theme_ button in the lower-left corner. Then click on the theme you want to export.

![Export theme dialog](export-theme-dialog-window.png)

## Example of custom themes

In this example the `-jr-theme` CSS property for the _Light_ theme has been changed from the normal blue (#50618F) to red (#8F0D11)

![Red Light theme](custom-theme-red.png)

In this example the `-jr-theme` CSS property for the _Light_ theme has been changed from the normal blue (#50618F) to green (#008f02)

![Green Light theme](custom-theme-green.png)

## Creating a new theme

The custom CSS theme is applied on top of the standard _Light_ theme which means that your custom CSS file does not need to contain all the properties that JabRef needs, just add the once that you want to change.

**If you want to know which CSS properties JabRef uses please export one of the base themes.**

## Selection of Useful CSS selectors

| UI element                       | CSS selector       |
| -------------------------------- | ------------------ |
| preview box                      | `#previewBody`     |
| `{} biblatex source` tab         | `.code-area`       |
| text in `{} biblatex source` tab | `.code-area .text` |

## Known bugs

* [#8523](https://github.com/JabRef/jabref/issues/8523): On Windows 10, it is not possible to use fonts that were installed user-wide in the CSS, only system-wide fonts are working. A workaround to use fonts that are not installed system-wide is to include the font file via [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face).
