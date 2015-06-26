#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0031. Rightmost Char
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	line=test.split(",")
	
	print line[0].find(str(line[1].rstrip()))

test_cases.close()

