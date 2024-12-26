note = int(input("Note eingeben (0-100): "))
erfahrung = int(input("Programmiererfahrung eingeben (1-5): "))

if note > 90:
    print("Einstellen")
elif erfahrung == 5 and note >= 70:
    print("Einstellen")
elif note > 70 or erfahrung == 4:
    print("Zum Gespräch einladen")
else:
    print("Ablehnen")