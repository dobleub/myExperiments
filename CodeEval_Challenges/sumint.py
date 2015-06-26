#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0024. Sum of Integers from a file
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l=test[0:(len(test)-1)]
	j=0
	for i in l:
		j+=int(i)
		
	print j

test_cases.close()
