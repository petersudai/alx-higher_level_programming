#!/usr/bin/python3

def uppercase(string):
    for char in string:
        uppercase_char = chr(ord(char) - ord('a') + ord('A')) if 'a' <= char <= 'z' else char
        print(uppercase_char, end="")
    print()
