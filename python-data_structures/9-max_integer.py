#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        for j in my_list:
            if j > i:
                return(j)
