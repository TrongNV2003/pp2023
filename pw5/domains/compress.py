import zipfile
import gzip
import os
print(os.getcwd())

class read:
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
        file_paths = os.path.join(dir_paths, 'students.dat')        
        with gzip.open(file_paths, "wb") as f:
            with open(students_file, "rb") as f1:
                f.write(f1.read())
            with open(courses_file, "rb") as f2:
                f.write(f2.read())
            with open(marks_file, "rb") as f3:
                f.write(f3.read())
    compress()

    def decompress():
        if os.path.isfile("students.dat"):
            with zipfile.ZipFile("students.dat","r") as zip:
                zip.extractall()
        else:
            pass