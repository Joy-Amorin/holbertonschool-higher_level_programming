#!/usr/bin/python3
for n in range(10):
    for i in range(10):
        if n < i and n < 8:
            print("{0}{1}, ".format(n, i), end="")
        if n == 8 and i == 9:
            print("{0}{1}".format(n, i))
