from functools import reduce

# Sample data: List of student records
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
    {"name": "Bob", "age": 22, "grades": [60, 72, 68]},
    {"name": "Charlie", "age": 21, "grades": [90, 95, 92]},
    {"name": "Diana", "age": 19, "grades": [45, 50, 48]},
]

# Step 1: Use map to extract student names
student_names = list(map(lambda student: student['name'], students))
print("Student Names:", student_names)

# Step 2: Use filter to create a sublist of students who passed (average grade above 70)
passing_students = list(filter(lambda student: reduce(lambda x, y: x + y, student['grades']) / len(student['grades']) > 70, students))
print("Passing Students:", passing_students)

# Step 3: Use reduce to calculate the total sum of all grades
total_grades = reduce(lambda acc, student: acc + reduce(lambda x, y: x + y, student['grades']), students, 0)
print("Total Sum of Grades:", total_grades)

# Step 4: Chain operations to get names of students who passed
passing_student_names = list(map(lambda student: student['name'], filter(lambda student: reduce(lambda x, y: x + y, student['grades']) / len(student['grades']) > 70, students)))
print("Names of Passing Students:", passing_student_names)

# Chaining operations in a single line
# Get total number of passing grades
total_passing_grades = reduce(lambda acc, student: acc + reduce(lambda x, y: x + y, student['grades']), 
                               filter(lambda student: reduce(lambda x, y: x + y, student['grades']) / len(student['grades']) > 70, students), 
                               0)
print("Total Sum of Grades for Passing Students:", total_passing_grades)
