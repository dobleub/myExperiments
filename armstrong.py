#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0082. Armstrong Numbers

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	x = len(test) - 1
	a = map(int,test[:x])

	b = 0
	for i in a:
		b += i ** x

	if b == int(test[:x]):
		print True
	else:	
		print False

