# Input information of students
num_students = int(input("Enter number of students in a class: "))
students = []
for i in range(num_students):
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student_DoB = input("Enter student date of birth: ")
    students.append((student_name,student_id,student_DoB))

# Input information of the courses
num_courses = int(input("Enter number of courses: "))
courses = []
for i in range(num_courses):
    course_name = input("Enter name of course: ")
    course_id = input("Enter ID of course: ")
    courses.append((course_name,course_id))

# Print the list of students and their information
def print_students():
    print("List of students: ")
    for student in students:
        print(f"Name: {student[0]}, ID: {student[1]}, Date of birth: {student[2]}")

# Print the list of courses and ID courses
def print_courses():
    for course in courses:
        print("List of courses: ")
        print(f"Course name: {course[0]}, ID: {course[1]}")

# Function to input marks for each student in a course
def input_marks():
    course_num = int(input("Enter the course number: "))
    course = courses[course_num-1]
    print(f"Input marks for course {course[0]} (ID: {course[1]}):")
    for i, student in enumerate(students):
        mark = int(input(f"Enter mark for {student[0]} (ID: {student[1]}): "))
        while marks < 0 or marks > 20:
            marks = float(input("Invalid marks entered! Please enter a marks from 0 and 20: "))
        students[i] += (mark,)

# Function to print the list of marks for each student in a course
def print_marks():
    course_num = int(input("Enter the course number: "))
    course = courses[course_num-1]
    print(f"List of marks for course {course[0]} (ID: {course[1]}):")
    for student in students:
        print(f"{student[0]} (ID: {student[1]}) - Mark: {student[course_num+2]}")

# Select a course and input marks for each student in that course
selected_course = input("Select a course to input marks for: ")
for student in students:
    marks = float(input(f"Enter marks (out of 20) for {student[0]} in {selected_course}: "))
    while marks < 0 or marks > 20:
        marks = float(input("Invalid marks entered! Please enter a marks from 0 and 20: "))
    print(f"Marks for {student[0]} in {selected_course}: {marks}")

# Menu option
while True:
    print("1. List of students")
    print("2. List of courses")
    print("3. Input marks for a course")
    print("4. List of marks for a course")
    print("5. End")
    choice = input("Choose your option: ")
    if choice == "1":
        print_students()
    elif choice == "2":
        print_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        print_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")