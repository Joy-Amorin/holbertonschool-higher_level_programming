#!/usr/bin/python3
def element_at(my_list, idx):
    for i in list(my_list):
        if idx < 0 and idx > idx + 1:
            return(None)
        else:
            return(idx + 1)
