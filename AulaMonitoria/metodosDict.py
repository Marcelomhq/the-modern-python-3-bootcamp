students = ['john','paul','bob']
students = {name: {'dob': None, 'grades': []} for name in students}

students['john']['dob'] = '31/10/1982'
students['john']['grades'].append(10) 
print(students)

print(students['john'].keys())
print(students['john'].values())
print(students['john'].items())

# print(students['joao'])
# print(students.get('joao'))

students.update({
    'pedro':{
        'dob':'10/10/1910',
        'grades':[10,9,3]
        }
    })

print(students)

# students['pedro']['grades'].clear()
# students['pedro']['grades'] = None
# students['pedro']['grades'] = []
print(students['pedro'].pop('grades'))

print(students)