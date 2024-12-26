def bewerber_pruefen(alter, abschlussnote):
    if 20 <= alter <= 50 and abschlussnote >= 80:
        return "einstellen"
    else:
        return "ablehnen"

# Test
alter = int(input("Bitte geben Sie das Alter des Bewerbers ein: "))
abschlussnote = float(input("Bitte geben Sie die Abschlussnote des Bewerbers ein: "))

ergebnis = bewerber_pruefen(alter, abschlussnote)
print(ergebnis)