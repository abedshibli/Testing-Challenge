import os
import subprocess

import pytest

#Variables
exe_path='C:/Users/abed/PycharmProjects/pythonProject/a.exe'

class v_functions():

#this function is to change the global value in main.c file
    @pytest.fixture
    def change_main_values(self,old_value,new_value):
        reading_file = open("main.c", "r")
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line.replace(old_value,new_value)
            new_file_content += new_line + "\n"
        reading_file.close()
        writing_file = open("main.c", "w")
        writing_file.write(new_file_content)
        writing_file.close()

#this function is to compile main.c and create exe
    def compile_c_file(self):
        return subprocess.call(["gcc", "main.c"])

#this function is to execute exe file
    @pytest.fixture
    def execute_c_exe(self):
        self.compile_c_file()
        tmp = subprocess.call("./a.exe")
        return tmp








