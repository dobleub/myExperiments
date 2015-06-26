#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0067. Hex to Decimal

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l0 = test.split(",")
	l0 = map(int,l0)
	
	l1 = l0[0] / l0[1]
	l2 = l1 * l0[1]
	l2 = l0[0] - l2
	
	print l2
