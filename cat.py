#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 23:26:24 2018

@author: ozzycodes
"""

# Create own version of the UNIX function 'cat'
import string
import sys
from optparse import OptionParser

"""
# Simple, single argument function of cat.py to read a single file:

file = open(sys.argv[1], "r")
for line in fileinput.input():
    print(line, end="")
"""

usage = "usage: %prog[option]... [file]..."
parser = OptionParser(usage=usage)
parser.add_option("-E", dest="show_end", action="store_true", help="Show $ at line endings")
parser.add_option("-n", dest="show_num", action="store_true", help="Show line numbers")
(options, args) = parser.parse_args()

if len(args) > 1:
    for a in args:
        f = open(a, "r")
else:
    []
string.rstrip()
