#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return(None)
    for i in my_list:
        if i == idx:
            my_list.remove(my_list[i])
        return(my_list)
    if idx > 0:
        return(my_list)
    if idx > len(my_lis):
        return(my_list)
    if idx == len(my_list):
        return(my_list)