from csv import DictWriter, writer
with open("example.csv", 'w', newline='') as file:
    headers = ["State", "Capital"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "State": "Paraiba"
        
    })