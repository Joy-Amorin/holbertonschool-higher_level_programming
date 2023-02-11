#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


import json
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

my_list = []

for arg in args:
    my_list.append(arg)

filename = 'add_item.json'

if not os.path.exists(filename):
    open(filename, 'w').close()

save_to_json_file(my_list, filename)
my_list = load_from_json_file(filename)
