#!/usr/bin/python3
"""fuction that writes an object to a text file
using JSONrepresentation"""


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
new_list = load_from_json_file(filename)
