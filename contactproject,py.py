import csv
import os

# Dateiname für die CSV-Datei
csv_file = "contacts.csv"


# Funktion zum Hinzufügen eines Kontakts
def add_contact():
    nachname = input("Nachname: ")
    vorname = input("Vorname: ")
    email = input("Email: ")
    telefonnummer = input("Telefonnummer: ")

    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([nachname, vorname, email, telefonnummer])

    print("Kontakt hinzugefügt.")


# Funktion zum Anzeigen aller Kontakte
def list_contacts():
    if not os.path.exists(csv_file):
        print("Keine Kontakte vorhanden.")
        return

    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("Nachname:", row[0])
            print("Vorname:", row[1])
            print("Email:", row[2])
            print("Telefonnummer:", row[3])
            print("-" * 20)


# Funktion zum Bearbeiten eines Kontakts
def edit_contact():
    nachname = input("Nachname des zu bearbeitenden Kontakts: ")

    contacts = []
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)

    found = False
    for index, contact in enumerate(contacts):
        if contact[0] == nachname:
            found = True
            print("Aktuelle Daten:")
            print("Vorname:", contact[1])
            print("Email:", contact[2])
            print("Telefonnummer:", contact[3])

            vorname = input("Neuer Vorname (Enter drücken, um nicht zu ändern): ")
            email = input("Neue Email (Enter drücken, um nicht zu ändern): ")
            telefonnummer = input("Neue Telefonnummer (Enter drücken, um nicht zu ändern): ")

            if vorname:
                contacts[index][1] = vorname
            if email:
                contacts[index][2] = email
            if telefonnummer:
                contacts[index][3] = telefonnummer

            with open(csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(contacts)

            print("Kontakt bearbeitet.")
            break

    if not found:
        print("Kontakt nicht gefunden.")


# Funktion zum Löschen eines Kontakts
def delete_contact():
    nachname = input("Nachname des zu löschenden Kontakts: ")

    contacts = []
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)

    found = False
    for index, contact in enumerate(contacts):
        if contact[0] == nachname:
            found = True
            del contacts[index]

            with open(csv_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(contacts)

            print("Kontakt gelöscht.")
            break

    if not found:
        print("Kontakt nicht gefunden.")


# Hauptfunktion
def main():
    while True:
        print("\nKontaktverwaltung")
        print("1. Kontakt hinzufügen")
        print("2. Kontakte anzeigen")
        print("3. Kontakt bearbeiten")
        print("4. Kontakt löschen")
        print("5. Beenden")

        choice = input("Bitte wählen Sie eine Option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    main()
