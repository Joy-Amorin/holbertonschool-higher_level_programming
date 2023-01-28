#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    x = my_list[idx]
    for i in my_list:
        if i == x:
            my_list.remove(my_list[x])
        return(my_list)
    if idx > 0:
        return(my_list)
    if idx > len(my_lis):
        return(my_list)
