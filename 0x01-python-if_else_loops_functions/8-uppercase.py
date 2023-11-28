#!/usr/bin/python3

def uppercase(string):
    for char in string:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' sle char
        print(uppercase_char, end="")
        print()
