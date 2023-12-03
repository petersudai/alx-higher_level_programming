#!/usr/bin/python3

import dis

def print_hidden_names():
    with open("hidden_4.pyc", "rb") as file:
        magic = file.read(4)
        file.readline()
        bytecode = file.read()

    for instruction in code:
        if instruction.opname == 'LOAD_GLOBAL' and not instruction.argrepr.startswith(('__')):
            names.add(instruction.argrepr)

    sorted_names = sorted(names)
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_names()
