#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    result = add(a, b) + sum(add(add(a, b), i) for i in range (4, 6)) if a < b else sub (a, b)

    return result
