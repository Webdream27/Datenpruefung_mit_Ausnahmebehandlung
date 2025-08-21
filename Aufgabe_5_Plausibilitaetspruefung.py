""" ************************************************
Eine Klasse fuer Wein
Jetzt mit eigener Ausnahmebehandlung
************************************************""" 

# Definition der eigenen Ausnahmeklasse
class IllegalArgumentException(Exception):
    pass

class Wein:
    # die Methode __init__()
    def __init__(self, alter, grundpreis):
        # Die Plausibilitaetspruefung fuer das Alter
        # Wenn der Wert ungueltig ist, wird eine Ausnahme ausgeloest 
        if alter <= 0:
            raise IllegalArgumentException("FEHLER: Das Alter muss ein positiver Wert sein.")
        self.alter = alter

        # und auch fuer den Preis
        if grundpreis <= 9:
            raise IllegalArgumentException("FEHLER: Der Grundpreis muss größŸer als 9 sein.")
        self.grundpreis = grundpreis
      
    # die Methode berechnet den Preis pro Flasche
    def preis_berechnen(self):
        self.preis_pro_flasche = self.alter * self.grundpreis
        
    # die Methode liefert den Preis pro Flasche
    def preis_liefern(self):
        self.preis_berechnen()
        return self.preis_pro_flasche

# --- Test der Ueberarbeiteten Klasse ---

# Versuch, eine Instanz mit gueltigen Werten zu erzeugen
try:
    print("Erzeuge eine gültige Flasche Wein...")
    flasche1 = Wein(10, 20.5)
    print("Preis der gültigen Flasche:", flasche1.preis_liefern())
except IllegalArgumentException as e:
    print(e)

print("-" * 30)

# Versuch, eine Instanz mit ungueltigem Alter zu erzeugen
# Die Ausnahme wird mit einem try-except-Block behandelt 
try:
    print("Erzeuge eine Flasche Wein mit ungültigem Alter...")
    flasche2 = Wein(-10, 20.5)
    print(flasche2.preis_liefern())
except IllegalArgumentException as e:
    # Die Fehlermeldung der Ausnahme ausgeben 
    print(e)

print("-" * 30)

# Versuch, eine Instanz mit ungueltigem Preis zu erzeugen
try:
    print("Erzeuge eine Flasche Wein mit ungültigem Preis...")
    flasche3 = Wein(15, 5)
    print(flasche3.preis_liefern())
except IllegalArgumentException as e:
    print(e)

