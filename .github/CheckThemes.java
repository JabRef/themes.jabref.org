///usr/bin/env jbang "$0" "$@" ; exit $?
//JAVA 25
//DEPS org.openjfx:javafx-base:26:${os.detected.jfxname}
//DEPS org.openjfx:javafx-graphics:26:${os.detected.jfxname}

import javafx.css.CssParser;
import javafx.css.Stylesheet;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/// Checks every theme against the CSS parser JavaFX itself uses, so a theme that JabRef
/// would silently ignore -- a syntax error, a media query it cannot read, or a color token
/// JabRef no longer knows -- fails here instead of in a user's JabRef.
public class CheckThemes {
    private static final Pattern TOKEN_READ = Pattern.compile("(-color-[a-z0-9-]*[a-z0-9])(?![a-z0-9-])(?!\\s*:)");

    /// Raw color ramps a theme may lay out for its own use, as the Primer theme does with AtlantaFX's.
    private static final Pattern PALETTE_RAMP = Pattern.compile("-color-(?:base|accent|success|warning|danger)-[0-9]|-color-(?:dark|light)");

    /// The JabRef theme declares the complete token contract, so it names every `-color-*` token a
    /// theme can meaningfully override. JabRef's base stylesheet only reads tokens, never declares one.
    private static final String JABREF_THEME = "JabRef/jabref-theme.css";

    public static void main(String[] args) throws Exception {
        Set<String> knownTokens = new TreeSet<>();
        collectTokens(new CssParser().parse(Path.of(args[0], JABREF_THEME).toUri().toURL()), knownTokens);
        System.out.println("JabRef declares " + knownTokens.size() + " color tokens.");

        List<Path> files = new ArrayList<>();
        try (var walk = Files.walk(Path.of(args[0]))) {
            walk.filter(path -> path.toString().endsWith(".css")).sorted().forEach(files::add);
        }
        if (files.isEmpty()) {
            System.err.println("No theme found below " + args[0]);
            System.exit(1);
        }

        int failed = 0;
        for (Path file : files) {
            Stylesheet stylesheet = new CssParser().parse(file.toUri().toURL());
            int rules = stylesheet.getRules().size();
            int declarations = stylesheet.getRules().stream().mapToInt(rule -> rule.getDeclarations().size()).sum();
            // A theme that parses into nothing applies nothing; JavaFX reports that as an empty
            // stylesheet rather than as an error.
            boolean ok = rules > 0 && declarations > 0;

            Set<String> unknown = new TreeSet<>();
            collectTokens(stylesheet, unknown);
            unknown.removeAll(knownTokens);
            // A theme may bring a vocabulary of its own -- the Primer theme carries AtlantaFX's --
            // as long as it reads those tokens itself. What stays is a token nothing can ever read:
            // a typo, or a leftover of a theme written against another JabRef version.
            unknown.removeAll(tokensRead(Files.readString(file)));
            unknown.removeIf(token -> PALETTE_RAMP.matcher(token).matches());
            ok &= unknown.isEmpty();

            if (!ok) {
                failed++;
            }
            System.out.printf("%-4s %2d rule(s), %3d declaration(s)  %s%n", ok ? "ok" : "FAIL", rules, declarations, file);
            if (!unknown.isEmpty()) {
                System.out.println("     unknown token(s): " + String.join(", ", unknown));
            }
        }

        System.out.println(failed == 0 ? "All " + files.size() + " themes are fine."
                : failed + " theme(s) apply nothing or set a token JabRef does not know.");
        System.exit(failed == 0 ? 0 : 1);
    }

    private static void collectTokens(Stylesheet stylesheet, Set<String> into) {
        stylesheet.getRules().forEach(rule -> rule.getDeclarations().forEach(declaration -> {
            // -jr-* are the JabRef 5.x variables; they are gone and JabRef ignores them without a word.
            if (declaration.getProperty().startsWith("-color-") || declaration.getProperty().startsWith("-jr-")) {
                into.add(declaration.getProperty());
            }
        }));
    }

    /// Every `-color-*` token the stylesheet reads, i.e. mentioned somewhere other than left of a colon.
    private static Set<String> tokensRead(String css) {
        Set<String> read = new TreeSet<>();
        Matcher matcher = TOKEN_READ.matcher(css.replaceAll("(?s)/\\*.*?\\*/", " "));
        while (matcher.find()) {
            read.add(matcher.group(1));
        }
        return read;
    }

}
