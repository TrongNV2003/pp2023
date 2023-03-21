import zipfile
import os
print(os.getcwd())

class read:
    def compress():
        # read the text to the same directory
        dir_paths = os.path.dirname(os.path.realpath(__file__))
        file_paths = os.path.join(dir_paths, 'students.dat')        
        with zipfile.ZipFile(file_paths, 'w') as f_out:
            with open('students.txt', 'r') as f_in:
                f_out.write(f_in.read())

            with open('courses.txt', 'r') as f_in:
                f_out.write(f_in.read())
                
            with open('marks.txt', 'r') as f_in:
                f_out.write(f_in.read())

    def decompress():
        if os.path.isfile("students.dat"):
            with zipfile.ZipFile("students.dat","r") as zip:
                zip.extractall()
        else:
            pass