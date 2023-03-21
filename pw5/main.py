from domains.student import Student
from domains.course import Course
from domains.classroom import Classroom
from input import *
from output import *
from domains.compress import read

classroom = Classroom()

read.decompress()

# Input information of students
num_students = int(input_num_students())
for i in range(num_students):
    student_name = input_student_name()
    student_id = input_student_id()
    student_DoB = input_student_dob()
    student = Student(student_name, student_id, student_DoB)
    classroom.add_student(student)
classroom.write_students_txt(student)

# Input information of the courses
num_courses = int(input_num_courses())
for i in range(num_courses):
    course_name = input_course_name()
    course_id = input_course_id()
    credits = input_course_credits()
    course = Course(course_name, course_id, credits)
    classroom.add_course(course)
classroom.write_courses_txt(course)

read.compress()

# Menu option
while True:
    print_menu()
    choice = input_menu_choice()
    if choice == '1':
        classroom.print_students()
    elif choice == '2':
        classroom.print_courses()
    elif choice == '3':
        classroom.input_marks()
    elif choice == '4':
        classroom.print_marks()
    elif choice == '5':
        classroom.calculate_gpa()
    elif choice == '6':
        break
    else:
        print_invalid_choice()
