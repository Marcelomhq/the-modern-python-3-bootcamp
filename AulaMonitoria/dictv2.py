students = {
    "Alice": {"Math": 85, "History": 90},
    "Bob": {"Math": 78, "History": 88}
}

def add_course(student_name, course, grade):
    if student_name in students:
        students[student_name][course] = grade
    else:
        students[student_name] = {course: grade}

def average_grade(student_name):
    if student_name in students:
        grades = students[student_name].values()
        return sum(grades) / len(grades)
    return "Student not found"

add_course("Alice", "Science", 95)
print(students) 
print(average_grade("Alice"))