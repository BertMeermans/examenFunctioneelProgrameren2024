import doktersIO
from prettytable import PrettyTable


def main():
    role = ''
    dokters = doktersIO.laad()
    while True:
        if not role in ['1', '2', '3']:
            print("1. User")
            print("2. Admin")
            print("3. Exit")
            role = input("Voer het nummer van de gewenste taak in (1-3): ")
        if role == '1':
            print("1. Toon alle dokters")
            print("2. Toon alle dokters van een ziekenhuis")
            print("3. Toon alle dokters met een specialisatie")
            print("4. Sorteer dokters volgens consultatieprijs (duurste eerst)")
            print("5. Zoek hulp")
            print("6. Logoff")
            keuze = input("Voer het nummer van de gewenste taak in (1-6): ")

            if keuze == '1':
                toon_alle_dokters(dokters)
            elif keuze == '2':
                toon_dokters_van_ziekenhuis(dokters, input("kies een ziekenhuis: "))
            elif keuze == '3':
                toon_dokters_met_specialisatie(dokters, input("kies een specialisatie: "))
            elif keuze == '4':
                sorteer_dokters_op_consultatiepijst(dokters)
            elif keuze == '5':
                zoek_hulp(dokters)
            elif keuze == '6':
                role = ''
            else:
                print("keuze niet gevonden")
        elif role == '2':
            print("1. Voeg dokter(s) toe")
            print("2. Verwijder een dokter")
            print("3. Verander de specialisatie van de dokter")
            print("4. Verander consultatieprijs van dokter")
            print("5. Update data (schrijf naar CSV)")
            print("6. Logoff")

            keuze = input("Voer het nummer van de gewenste taak in (1-6): ")

            if keuze == '1':
                voeg_dokters_toe(dokters)
            elif keuze == '2':
                verwijder_dokter(dokters, selecteer_een_dokter(dokters))
            elif keuze == '3':
                verander_specialisatie(dokters, selecteer_een_dokter(dokters), input("geef de nieuwe instrument: "))
            elif keuze == '4':
                verander_consultatieprijs(dokters, selecteer_een_dokter(dokters),
                                          int(input("geef de nieuwe consultatieprijs in: ")))
            elif keuze == '5':
                doktersIO.bewaar(dokters)
            elif keuze == '6':
                role = ''
            else:
                print("keuze niet gevonden")
        elif role == '3':
            exit()
        else:
            print("foute keuze, probeer opnieuw")


def toon_alle_dokters(dokters):
    table = PrettyTable()
    table.field_names = ['Name', 'Ziekenhuis', 'Specialisatie', 'Consultatieprijs']
    for dokter, details in dokters.items():
        table.add_row([dokter, details.get('ziekenhuis', ''),
                       details.get('specialisatie', ''), details.get('consultatieprijs', '')])
    print(table)


def toon_dokters_van_ziekenhuis(dokters, ziekenhuis):
    matching_dokters = {name: details for name, details in dokters.items() if
                        details['ziekenhuis'].lower() == ziekenhuis.lower()}
    print(f"dokters van ziekenhuis '{ziekenhuis}':")
    toon_alle_dokters(matching_dokters)


def toon_dokters_met_specialisatie(dokters, specialisatie):
    matching_dokters = {name: details for name, details in dokters.items() if
                        details['specialisatie'].lower() == specialisatie.lower()}
    print(f"dokters met specialisatie '{specialisatie}':")
    toon_alle_dokters(matching_dokters)


def sorteer_dokters_op_consultatiepijst(dokters):
    sorted_dokters = dict(sorted(dokters.items(), key=lambda x: x[1]['consultatieprijs'], reverse=True))
    print("dokters gesorteerd op consultatieprijs (duurste eerst):")
    toon_alle_dokters(sorted_dokters)


def zoek_hulp(dokters):
    ziekenhuis = input("Geef het ziekenhuis in: ").lower()
    specialisatie = input("Geef de specialisatie: ").lower()

    matching_dokters = dict(filter(lambda x: (x[1]['ziekenhuis'].lower() == ziekenhuis and x[1]['specialisatie'].lower() == specialisatie), dokters.items()))
    if len(matching_dokters) == 0:
        print("Geen dokters gevonden")
    else:
        toon_alle_dokters(matching_dokters)

def voeg_dokters_toe(dokters):
    aantal_toevoegen = int(input("Voer het aantal dokters in dat je wilt toevoegen: "))
    for _ in range(aantal_toevoegen):
        name = input("Voer de naam van de dokter in: ")
        while name in dokters.keys():
            name = input("deze dokter bestaat al probeer een ander naam: ")
        ziekenhuis = input(f"Voer het ziekenhuis van {name} in: ")
        specialisatie = input(f"Voer het specialisatie van {name} in: ")
        consultatieprijs = int(input(f"Voer de consulatieprijs van {name} in: "))
        dokters[name] = {'ziekenhuis': ziekenhuis, 'specialisatie': specialisatie, 'consultatieprijs': consultatieprijs}
        print()
    print(f"{aantal_toevoegen} dokters toegevoegd.")


def verwijder_dokter(dokters, naam):
    if naam in dokters:
        del dokters[naam]
        print(f"Dokter '{naam}' verwijderd.")
    else:
        print(f"Dokter '{naam}' niet gevonden.")


def verander_specialisatie(dokters, naam, nieuwe_specialisatie):
    if naam in dokters:
        dokters[naam]['specialisatie'] = nieuwe_specialisatie
        print(f"Specialisatie van dokter '{naam}' veranderd naar '{nieuwe_specialisatie}'.")
    else:
        print(f"Dokter '{naam}' niet gevonden.")


def verander_consultatieprijs(dokters, naam, nieuwe_consultatieprijs):
    if naam in dokters:
        dokters[naam]['consultatieprijs'] = nieuwe_consultatieprijs
        print(f"Consultatieprijs van dokter '{naam}' veranderd naar {nieuwe_consultatieprijs}.")
    else:
        print(f"Dokter '{naam}' niet gevonden.")


def selecteer_een_dokter(dokters):
    tabel = PrettyTable()
    tabel.field_names = ["Nr", "Naam"]
    rows = [name for name in dokters.keys()]
    tabel.add_rows([index, name] for index, name in enumerate(rows))
    print(tabel)
    keuze = int(input("Kies een dokter [nr]: "))
    return rows[keuze]


if __name__ == "__main__":
    main()
