#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:31:13 2017

@author: aspen
"""

def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers")
    elif n < 0:
        print("Factorial is only defined for positive integers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))
print(factorial(3.2))
print(factorial(-3))