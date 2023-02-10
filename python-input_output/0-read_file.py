#!/usr/bin/python3
"""reads a text file andprints it to stdout"""


def read_file(filename=""):
    """functions that reads"""

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
    f.close()
