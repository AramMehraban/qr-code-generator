import qrcode

def generiere_qr_code():
    print("Willkommen beim QR-Code Generator!")
    # 1. Benutzereingabe abfragen
    daten = input("Bitte gib einen Text oder eine URL ein: ")
    dateiname = input("Wie soll die Bilddatei heißen? (z.B. code.png): ")

# Wenn der User .png vergisst, fügen wir es an
    if not dateiname.endswith('.png'):
        dateiname += '.png'

    # 2. QR-Code konfigurieren (optional, macht den Code aber robuster/schöner)
    qr = qrcode.QRCode(
        version=1, # Größe des Codes (1 bis 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L, # Fehlerkorrektur-Level
        box_size=10, # Größe der einzelnen Kästchen
        border=4, # Randbreite
    )

    # 3. Daten hinzufügen und QR-Code generieren
    qr.add_data(daten)
    qr.make(fit=True)

    # 4. Bild erstellen (Hier ist die Bonus-Lösung mit Farben versteckt!)
    img = qr.make_image(fill_color="black", back_color="white")

    # 5. Bild speichern
    img.save(dateiname)
    print(f"Erfolg! Der QR-Code wurde als '{dateiname}' gespeichert.")

# Das Skript ausführen
if __name__ == "__main__":
    generiere_qr_code()
