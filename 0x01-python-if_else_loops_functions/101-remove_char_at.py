#!/usr/bin/python3

def remove_char_at(s, n):
    result = ""
    i = 0
    for c in s:
        if i != n:
            result += c
        i += 1
    return result
