import math
import numpy as np
import os
print(os.getcwd())

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []
        self.credits = []               
    
    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

# Write student information to students.txt          
    def write_students_txt(self,student):
        # get the text to the same directory
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "students.txt")
        
        with open(file_path, "w") as f:    
            for student in self.students:
                f.write(f"Name: {student.name},ID: {student.student_id},DOB: {student.date_of_birth}\n")

# Write courses information to courses.txt 
    def write_courses_txt(self, course):
        # get the text to the same directory 
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "courses.txt")
        
        with open(file_path, "w") as f:
            for course in self.courses:
                f.write(f"Course name: {course.name},ID: {course.course_id},Credit: {course.credits}\n")

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

# input marks for students in the courses
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
        
# get the text to the same directory 
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "marks.txt")    

# Write mark information to marks.txt
        with open(file_path, 'w') as f:
            for course in self.courses:
                f.write(f"Course name: {course.name}, ID: {course.course_id}\n")  
                for student in self.students:
                    mark = student.get_mark(course.course_id)
                    f.write(f"Student name: {student.name},ID: {student.student_id},Mark: {mark}\n")
                    
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