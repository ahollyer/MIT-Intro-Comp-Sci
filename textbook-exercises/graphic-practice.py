#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:50:09 2017

@author: aspen
"""

from graphics import *

win = GraphWin()

p = Point(50, 60)
print(p.getX())
print(p.getY())
p.draw(win)
p2 = Point(140,100)
p2.draw(win)