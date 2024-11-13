# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science"
# }

# student["age"] = 21  
# student["grade"] = "A"  
# del student["major"]  


# print(student)

# students = {
#     "John": {
#         "dob": "2000-01-01",
#         "grades": [85, 90, 78]
#     },
#     "Paul": {
#         "dob": "2001-03-15",
#         "grades": [88, 76, 95]
#     },
#     "Bob": {
#         "dob": "2002-05-22",
#         "grades": [92, 88, 84]
#     }
# }
# print(students["John"])  


students = ['john','paul','bob']
students = {name: {'dob': None, 'grades': []} for name in students}

students['john']['dob'] = '31/10/1982'
students['john']['grades'].append(10) 
print(students)