#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	m = len(test)-1
	l = test[:m]
	l = list(l)
	l1 = []
	[ l1.append(int(i)) for i in l if int(i) not in l1]
	
	print l1
