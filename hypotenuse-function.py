#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:56:50 2017

@author: aspen
"""

import math

def hypotenuse(a, b):
    c_squared = a**2 + b**2
    c = math.sqrt(c_squared)
    return c

print(hypotenuse(2, 3))