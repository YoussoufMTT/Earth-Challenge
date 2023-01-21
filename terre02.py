import os

path = os.path.abspath(__file__)

file_list = path.split('/')

file_name = file_list[len(file_list) - 1]

print(file_name)