import javafx.css.CssParser;
import javafx.css.Stylesheet;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/// Parses every theme with the CSS parser JavaFX itself uses, so a theme that JabRef
/// would silently ignore -- a syntax error, or a media query it cannot read -- fails
/// here instead of in a user's JabRef.
public class CheckThemes {
    public static void main(String[] args) throws Exception {
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
            if (!ok) {
                failed++;
            }
            System.out.printf("%-4s %2d rule(s), %3d declaration(s)  %s%n", ok ? "ok" : "FAIL", rules, declarations, file);
        }

        System.out.println(failed == 0 ? "All " + files.size() + " themes parse." : failed + " theme(s) apply nothing.");
        System.exit(failed == 0 ? 0 : 1);
    }
}
