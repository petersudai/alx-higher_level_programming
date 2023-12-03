#!/usr/bin/python3

def magic_calculation(a, b):
    m = __import__('magic_calculation_102', fromlist=('add','sub'))
    add, sub == m.add, m.sub
    return (lambda c=a: sum(add(c, i) for i in range(4, 6)) if c < b else sub(a, b))()
    
