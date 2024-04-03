from Objects import parser_functions, get_data
import os
from OutputValidator import v_functions, exe_path


class Test_Validator_Parser:
    # Test to verify if the JSON file is created in the path
    def test_verify_csv_json_dump(self):
        parser_functions.json_dumps()
        assert os.path.isfile(exe_path) == 1

    # Test to verify if printing the users names
    def test_verify_users_printed(self):
        assert parser_functions.json_users(get_data("Var1")) == get_data("Var1")

    # Test to verify if printing the users names and their commands
    def test_verify_users_commands_printed(self):
        assert parser_functions.json_commands(get_data("Var1"),get_data("Var2")) == (get_data("Var1"), get_data("Var2"))

    # Test to verify if printing the command by pid
    def test_verify_commands_by_pid(self):
        assert parser_functions.get_command_by_pid(get_data("Process")) == '"rcu_gp"'

    # Test to verify top five commands by memory usage
    def test_verify_topfive_printed(self):
        assert parser_functions.json_max_five() == 5

    # Test to verify if the exe output match given value
    def test_verify_c_exe_output(self, value):
        v_functions.change_main_values("__VALUE__", "123")
        assert v_functions.execute_c_exe() == value
    # Test to verify if the exe is created
    def test_verify_exe_created(self):
        assert os.path.isfile(exe_path) == 1


#Main function
#to run main function type in the terminal : python nameoffile.py for example: python OutputValidator.py
#if no output in terminal tests under main function are passed otherwise if a test fails an output in the terminal will be seen
#note: we can use pytest for more verbosed output type the command: pytest -s -v OutputValidator.py

if __name__ == '__main__':
    Test_Validator_Parser().test_verify_csv_json_dump()
    Test_Validator_Parser().test_verify_users_printed()
    Test_Validator_Parser().test_verify_users_commands_printed()
    Test_Validator_Parser().test_verify_commands_by_pid()
    Test_Validator_Parser().test_verify_topfive_printed()
    Test_Validator_Parser().test_verify_c_exe_output()
    Test_Validator_Parser().test_verify_exe_created()



