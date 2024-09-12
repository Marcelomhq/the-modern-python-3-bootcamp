'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import DictWriter
def add_user(file_name,first_name, last_name):
    with open(file_name, "a", newline='') as file:
        headers = ('First Name', 'Last Name')
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writerow({
            'First Name': first_name,
            'Last Name': last_name
            })


# add_user("ex1.csv", "Dwayne", "Johnson")
# from csv import DictWriter

# def add_user(file_name, first_name, last_name):
#     # Open the file in append mode
#     with open(file_name, "a", newline='') as file:
#         headers = ('First Name', 'Last Name')
#         csv_writer = DictWriter(file, fieldnames=headers)
        
#         # Simply write the user data (no need to write the header again)
#         csv_writer.writerow({
#             'First Name': first_name.strip(),
#             'Last Name': last_name.strip()
#         })

with open('ex1.csv', 'w', newline = '') as file:
    headers = ('First Name', 'Last Name')
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
            'First Name': 'Colt',
            'Last Name': 'Steele'
        })

add_user("ex1.csv", "Dwayne", "Johnson")
