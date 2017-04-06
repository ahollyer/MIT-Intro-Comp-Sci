#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 09:01:00 2017

@author: aspen
"""

# A simple program illustrating chaotic behavior

# Taken from Python Programming: An Introduction to Computer Science by John Zelle

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
        
main()