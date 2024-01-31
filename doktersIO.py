import csv

csv_file_path = "dokters.csv"


def bewaar(lijst):
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ["doktersnaam", "ziekenhuis", "specialisatie", "consultatieprijs"]
        writer = csv.writer(csv_file)
        writer.writerow(fieldnames)

        for key, item in lijst.items():
            writer.writerow([key, item['ziekenhuis'], item['specialisatie'], item.get('consultatieprijs', 0)])

    print(f"Dokter data is opgeslagen in {csv_file_path}.")


def laad():
    lijst = {}
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            lijst[row['doktersnaam']] = {
                'ziekenhuis': row['ziekenhuis'],
                'specialisatie': row['specialisatie'],
                'consultatieprijs': int(row['consultatieprijs'])
            }
    return lijst
