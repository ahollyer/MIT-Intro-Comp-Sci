#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:33:38 2017

@author: aspen
"""

#A program that accepts a principal amount, apr, and
#number of years, and returns the future value of the investment

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as a decimal: "))
    years = eval(input("Enter the number of years: "))
    
    for i in range(years):
        principal = principal * (1 + apr)
        
    print("The value in", years, "years is:", principal)
    
main()