#!/usr/bin/python3

def uppercase(s):
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            c = chr(ord(i) - 32)
        else:
            c = i
        print("{}".format(c), end="")
        print()
