#!/usr/bin/env python3

def no_c(my_string):
    filt_string = ''.join(char for char in my_string if char.lower() != 'c')
    return filt_string
