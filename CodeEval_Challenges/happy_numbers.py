#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0039. Happy Numbers

import sys

test_cases = open(sys.argv[1], 'r')


for test in test_cases:
	m = len(test) - 1
	l = int(test[:m])
	l = l ** 2
	#print l,
	
	while True:
		l1 = list(str(l))
		l1 = map(int,l1)
		l2 = [(i ** 2) for i in l1]
		l = sum(l2)
		#print l,
		if l == 1:
			print 1
			break
		elif l == 4:
			print 0
			break
		else:
			next
	
