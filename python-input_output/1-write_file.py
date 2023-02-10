#!/usr/bin/python3
"""write a string and return the numbers"""


def write_file(filename="", text=""):
    """fuction that write and return"""
    with open(filename, 'w') as f:
        ch_text = f.write(text)
        return(ch_text)
    f.close()
