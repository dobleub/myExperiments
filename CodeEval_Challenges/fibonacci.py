#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0022. Fobonacci
import sys

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:	
	print fibonacci(int(test))

test_cases.close()
