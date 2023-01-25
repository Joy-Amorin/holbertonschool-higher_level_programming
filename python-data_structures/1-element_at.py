#!/usr/bin/python3
def element_at(my_list, idx):
    for i in list(my_list):
        if idx < 0:
            return(None)
        if idx >= len(my_list):
            return(None)
        else:
            return(idx + 1)
