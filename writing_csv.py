from csv import writer, reader

with open("fighters.csv", "r") as file:
    csv_reader = reader(file)
    print(csv_reader)
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open('caps_fighters.csv', 'w', newline='') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)