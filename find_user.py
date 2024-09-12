
# find_user
# For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. 
# If the user is found, find_user  returns the index where the user 
# is found. Otherwise it returns a message stating that the user wasn't found.
import csv

def find_user(first_name, last_name):
    index = 0
    with open("user.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["First Name"] == first_name and row["Last Name"] == last_name:
                return index+1
            else:
                index +=1
        return "First and last name arent in the file"
    
print(find_user("Marcelo11","Queiroga"))