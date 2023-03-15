import math
import numpy as np
import curses

class Student:
    def __init__(self, name, student_id, date_of_birth):
        self.name = name
        self.student_id = student_id
        self.date_of_birth = date_of_birth
        self.marks = {}
        
    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id, 0)

class Course:
    def __init__(self, name, course_id, credits):
        self.name = name
        self.course_id = course_id
        self.credits = int(credits)

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []
        self.credits = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

# list information of students
    def print_students(self):
        print("----------------------------------------------")
        print("List of students: ")
        for student in self.students:
            print(f"Name: {student.name}, ID: {student.student_id}, Date of birth: {student.date_of_birth}")

# list information of courses
    def print_courses(self):
        print("----------------------------------------------")
        print("List of courses: ")
        for course in self.courses:
            print(f"Course name: {course.name}, ID: {course.course_id}, Credits: {course.credits}")

# add marks for students in the courses
    def input_marks(self):
        course_id = input("Enter the ID of the course: ")
        while course_id not in [c.course_id for c in self.courses]:
            print("Invalid ID course. Please try again")
            course_id = input("Enter the ID of the course: ")

        for course in self.courses:
            if course.course_id == course_id:
                print("----------------------------------------------")
                print(f"Input marks for course {course.name} (ID: {course.course_id}):")
                for student in self.students:
                    unround_down_mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
                    while unround_down_mark < 0 or unround_down_mark > 20:
                        unround_down_mark = float(input("Invalid marks entered! Please enter a marks from 0 and 20: "))
                    mark = math.floor(unround_down_mark * 10)/10    # round-down mark to 1 digit
                    student.add_mark(course_id, mark)
    
# calculate the GPA of each students
    def calculate_gpa(self):
        student_gpa = []
        
        for student in self.students:
            mark = np.array([student.get_mark(course.course_id) for course in self.courses])
            credits = np.array([course.credits for course in self.courses])
            weighted_marks = np.sum(mark * credits)
            total_credits = np.sum(credits)
            
            if total_credits > 0:
                unround_down_gpa = weighted_marks / total_credits
                gpa = math.floor(unround_down_gpa * 100)/100    # round down GPA to 2 digits
                student_gpa.append((gpa,student))
            else:
                print(f"Lack of marks for {student.name} (ID: {student.student_id})")
        
        student_gpa = sorted(student_gpa, reverse=True)     # Sort student list by GPA descending
        print("----------------------------------------------")
        print("Students GPA rankings: ")
        for i, (gpa, student) in enumerate(student_gpa, start = 1):
            print(f"{i}. {student.name} (ID: {student.student_id}) - GPA: {gpa}")
               
# list marks
    def print_marks(self):
        course_id = input("Enter the ID of the course: ")
        while course_id not in [c.course_id for c in self.courses]:
            print("Invalid ID course. Please try again")
            course_id = input("Enter the ID of the course: ")

        for course in self.courses:
            if course.course_id == course_id:
                print("----------------------------------------------")
                print(f"List of marks for course {course.name} (ID: {course.course_id}):")
        for student in self.students:
            mark = student.get_mark(course_id)
            print(f"{student.name} (ID: {student.student_id}) - Mark: {mark}")

classroom = Classroom()

# Input information of students
num_students = int(input("Enter number of students in a class: "))
for i in range(num_students):
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    student_DoB = input("Enter student date of birth: ")
    student = Student(student_name, student_id, student_DoB)
    classroom.add_student(student)

# Input information of the courses
num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    course_name = input("Enter name of course: ")
    course_id = input("Enter ID of course: ")
    credits = input("Enter number of credits of course: ")
    course = Course(course_name, course_id, credits)
    classroom.add_course(course)

# Menu option
while True:
    print("----------------------------------------------")
    print("1. List of students")
    print("2. List of courses")
    print("3. Input marks for a course")
    print("4. List of marks for a course")
    print("5. List the GPA of students")
    print("6. End")
    choice = input("Choose your option: ")
    if choice == "1":
        classroom.print_students()
    elif choice == "2": 
        classroom.print_courses()
    elif choice == "3":
        classroom.input_marks()
    elif choice == "4":
        classroom.print_marks()
    elif choice == "5":
        classroom.calculate_gpa()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")