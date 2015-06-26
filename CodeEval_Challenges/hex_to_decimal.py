#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0067. Hex to Decimal

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	m = len(test)-1
	l = str(test[:m])
	
	print int(l,16)
