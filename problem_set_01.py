#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:04:41 2017

@author: aspen
"""
#PSet 01: Create a program to compute & print the 1000th prime number

import math

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True;
        
primeCounter = 1 #because 2 is prime
x = 3

while primeCounter < 999:
    if isPrime(x):
        primeCounter += 1
        print(x, "is prime number", primeCounter)
    x += 2 #increment x by 2 for the next odd number
    
print(x, "is the 1000th prime number!")