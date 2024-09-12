from csv import DictReader
with open("fighters.csv", "r") as file:
    csv_read = DictReader(file)
    for row in csv_read:
        # print(f"Fighter: {row['Name']} from {row['Country']} and his height is {row['Height (in cm)']}cm")
        print(row)
