import csv
import json
import os


#variables
exe_path='C:/Users/abed/PycharmProjects/pythonProject/data.json'
class p_functions:

#function to dump csv to json
    def json_dumps(self):
        csvfile = open('top_linux.csv', 'r')
        jsonfile = open('data.json', 'w',encoding='utf-8')
        reader = csv.DictReader(csvfile)
        for row in reader:
           (json.dump(row,jsonfile,indent=4))
           jsonfile.write('\n')
        csvfile.close()

#function to print all users
    def json_users(self,var):
        csvfile = open('top_linux.csv', 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(json.dumps(row[var]))
        csvfile.close()
        return var

#function to print all users and their commands
    def json_commands(self,var1,var2):
        csvfile = open('top_linux.csv', 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(json.dumps(row[var1]),json.dumps(row[var2]))
        csvfile.close()
        return var1,var2

#function to print command by pid
    def get_command_by_pid(self,value):
        if type(value) is not str:
            raise TypeError("Only strings are allowed")
        csvfile = open('top_linux.csv', 'r')
        reader = csv.DictReader(csvfile)
        for row in reader:
            if value in json.dumps(row['PID']):
                return (json.dumps(row['COMMAND']))
        csvfile.close()

#function to print top five commands by memory usage
    def json_max_five(self):
        csvfile = open('top_linux.csv', 'r')
        reader = csv.DictReader(csvfile)
        count=0
        for row in reader:
            print(json.dumps(row['%MEM']),json.dumps(row['COMMAND']))
            count += 1
            if 'Xorg' in json.dumps(row['COMMAND']):
                break
        return count


