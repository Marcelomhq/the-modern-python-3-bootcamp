
# print_users
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# print_users : prints out all of the first and last names in the users.csv file
import csv
# import os

def print_users():
    # file_path = os.path.abspath("user.csv")
    # print(f"\n{file_path} \naaaaaaaaaa")
    with open("user.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        print('aloooo achei arquivo')
        for row in csv_reader:
            print(f"{row['First Name']} {row['Last Name']}")

print_users()