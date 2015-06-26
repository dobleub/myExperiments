#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0030. Set Intersection
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l0 = test.split(";")
	l1 = l0[0].split(",")
	l1 = map(int,l1)
	l2 = l0[1].split(",")
	l2 = map(int,l2)
	l3 = []
	[l3.append(n) for n in l2 if n in l1]
	
	l = [str(n) for n in l3]
	print ",".join(l)
	
test_cases.close()
