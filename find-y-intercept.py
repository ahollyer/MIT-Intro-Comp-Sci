#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:11:19 2017

@author: aspen
"""

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def y_intercept(x1, y1, x2, y2):
    ##slope-intercept form, y = mx + b
    ##solve for b: b = y - mx
    m = slope(x1, y1, x2, y2)
    b = y1 - m * x1
    return b

print(y_intercept(1, 5, 2, 7))