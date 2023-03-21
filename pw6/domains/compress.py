import os
import pickle
import gzip

class read:
    @staticmethod
    def compress():
        # take the files txt from the directory
        dir_path = os.path.dirname(os.path.realpath(__file__))
        students_file = os.path.join(dir_path, "students.txt")
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        courses_file = os.path.join(dir_path, "courses.txt")
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        marks_file = os.path.join(dir_path, "marks.txt")

        # read the text to the same directory
        dir_paths = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_paths, 'students.dat')        
        with gzip.open(file_path, "wb") as f:
            data = {
                "students": open(students_file, "rb").read(),
                "courses": open(courses_file, "rb").read(),
                "marks": open(marks_file, "rb").read(),
            }
            pickle.dump(data, f)

    @staticmethod
    def decompress():
        # take file from the same directory
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'students.dat')
        if os.path.isfile(file_path):
            with gzip.open(file_path, "rb") as f:
                data = pickle.load(f)
            with open(os.path.join(dir_path, "students.txt"), "wb") as f1:
                f1.write(data["students"])
            with open(os.path.join(dir_path, "courses.txt"), "wb") as f2:
                f2.write(data["courses"])
            with open(os.path.join(dir_path, "marks.txt"), "wb") as f3:
                f3.write(data["marks"])
