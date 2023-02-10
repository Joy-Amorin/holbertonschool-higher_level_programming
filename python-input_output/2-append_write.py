#!/usr/bin/python3
"""appennds a string at the end of a text file
and returns the numbers of characters added """


def append_write(filename="", text=""):
    """function that appennd a return """

    with open(filename, 'a') as f:
        append_txt = f.write(text)
        return(append_txt)
    f.close()
