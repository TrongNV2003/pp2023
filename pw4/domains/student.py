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
