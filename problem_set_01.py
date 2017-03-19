#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:04:41 2017

@author: aspen
"""

import math

##initialize possible primes
possiblePrimes = (1, 2)

##concatenate all possible primes from 3-1000
for n in range(3,1000):
    if n % 2 != 0:
        possiblePrimes += (n,)

print(possiblePrimes)