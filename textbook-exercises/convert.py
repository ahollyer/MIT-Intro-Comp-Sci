#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:39:59 2017

@author: aspen
"""

#A program to convert Celsius temperature to Fahrenheit

def main():
    print("This program converts Celsius to Fahrenheit.\n")
    c = eval(input("What is the Celsius temperature? "))
    f = 9/5 * c + 32
    print("The temperature is", f, "degrees Fahrenheit.")
        
main()
    
def table():
    print("This program prints a Celsius/Fahrenheit conversion table.\n")
    print("Celsius\t", "Fahrenheit")
    for t in range(0, 101, 10):
        c = t
        f = 9/5 * c + 32
        print(c, "\t", f)
        
table()