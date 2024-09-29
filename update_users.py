import csv

def update_user(first_name, last_name, new_first, new_last):
    users_updated = 0
    with open("user.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
        
    # Open the CSV file for writing
    with open("user.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        for row in rows:
            # Make sure the row is not empty and has at least two columns
            # if len(row) >= 2:
            if row[0] == first_name and row[1] == last_name:
                # Update first and last name
                csv_writer.writerow([new_first, new_last])
                users_updated += 1                   
            else:
                csv_writer.writerow(row)
            # else:
            #     # If row is empty or malformed, write it back unchanged
            #     csv_writer.writerow(row)
                                     
    return users_updated


print(update_user("Marcelo","Queiroga","Marc","Honorato"))
    
