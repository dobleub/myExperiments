#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0018. Multiples of a Number
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l = test.split(",")
	l = map(int,l)
	
	i = 0
	while True:
		if (l[1] * i) >= l[0]:
			print (l[1] * i)
			break
		else:
			i += 1
