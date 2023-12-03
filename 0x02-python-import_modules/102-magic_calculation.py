#!/usr/bin/python3

def magic_calculation(a, b):
    module = __import__('magic_calculation_102', fromlist=('add','sub'))
    add, sub == module.add, module.sub
    if a< b: c = add(a, b); c = sum(add(c, i) for i in range(4, 6)); return c
    return sub(a, b)
