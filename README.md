# Datenpruefung_mit_Ausnahmebehandlung
Python Datenprüfung mit Ausnahmebehandlung

Das Skript ist ein Beispiel für Exception Handling (Ausnahmebehandlung) in Python, das die Robustheit eines Programms verbessert. Anstatt bei ungültigen Daten einfach fortzufahren, wird ein Fehler explizit signalisiert.

IllegalArgumentException: Eine benutzerdefinierte Ausnahmeklasse, die spezifisch für ungültige Funktionsargumente verwendet wird.
Wein Klasse: Ihr Konstruktor (__init__) führt eine strenge Plausibilitätsprüfung durch. Wenn das Alter oder der Grundpreis unlogisch ist, wird eine IllegalArgumentException ausgelöst (raise).
Test-Code: Das Skript demonstriert die Ausnahmebehandlung mit try-except-Blöcken. Hier werden die ausgelösten Fehler abgefangen und verarbeitet, anstatt das Programm abstürzen zu lassen.

Dieses Projekt zeigt eine saubere Methode, um Eingabefehler zu behandeln und die Datenintegrität in einer Klasse zu gewährleisten.
