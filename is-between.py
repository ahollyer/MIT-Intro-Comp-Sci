#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:28:03 2017

@author: aspen
"""

def isBetween(x, lowerBound, upperBound):
    #accepts a number, a lower bound, and an upper bound, tests whether the
    #number falls within the bounds, and returns a boolean
    return lowerBound < x < upperBound

print(isBetween(3, 1, 5))
print(isBetween(10, 20, 90))
