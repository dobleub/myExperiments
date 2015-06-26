#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0029. Unique Elements
import sys
from string import join

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l = test.split(",")
	l1 = []
	[l1.append(int(n)) for n in l if int(n) not in l1]
	
	#for i in l:
	#	if int(i) not in l1:
	#		l1.append(int(i))
	
	l = [str(n) for n in l1]
	print ",".join(l)
	
test_cases.close()
