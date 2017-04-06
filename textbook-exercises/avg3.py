#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 10:49:53 2017

@author: aspen
"""

#avg3.py
#   A simple program to average 3 exam scores
#   Illustrates use of multiple input

def main():
    print("This program returns the average of three exam scores.\n")
    score1, score2, score3 = eval(input("Please enter the three scores separated by commas: "))
    avg = (score1 + score2 + score3) / 3
    print("Your exam average is:", avg)
    
main()