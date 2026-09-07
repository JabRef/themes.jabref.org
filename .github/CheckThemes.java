import javafx.css.CssParser;
import javafx.css.Stylesheet;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

/// Checks every theme against the CSS parser JavaFX itself uses, so a theme that JabRef
/// would silently ignore -- a syntax error, a media query it cannot read, or a color token
/// JabRef no longer knows -- fails here instead of in a user's JabRef.
public class CheckThemes {
    /// JabRef's own stylesheets on `main`, which between them declare every `-color-*` token
    /// a theme can meaningfully override.
    private static final List<String> TOKEN_SOURCES = List.of(
            "https://raw.githubusercontent.com/JabRef/jabref/main/jabgui/src/main/resources/org/jabref/gui/theme/jabref-theme.css",
            "https://raw.githubusercontent.com/JabRef/jabref/main/jabgui/src/main/resources/org/jabref/gui/theme/internal/jabref-base.css");

    public static void main(String[] args) throws Exception {
        Set<String> knownTokens = new TreeSet<>();
        for (String source : TOKEN_SOURCES) {
            collectTokens(new CssParser().parse(fetch(source)), knownTokens);
        }
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

    private static String fetch(String url) throws Exception {
        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(HttpRequest.newBuilder(URI.create(url)).build(), HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new IllegalStateException("HTTP " + response.statusCode() + " for " + url);
        }
        return response.body();
    }
}
