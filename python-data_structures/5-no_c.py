#!/usr/bin/python
def no_c(my_string):
    not_c = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            not_c = not_c + i
    return (not_c)