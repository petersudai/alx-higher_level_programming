#!/usr/bin/python3

def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return (s)
    i = 0
    result = ""
    for c in range(len(s)):
        if i != n:
            result += c
            i += 1

            return result
