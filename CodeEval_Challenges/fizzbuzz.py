#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0001. Fizz Buzz challenge
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	line=test.split()
	rangos=range(1,int(line[2])+1)
	
	for i in rangos:
		r1 = i % int(line[0])
		r2 = i % int(line[1])
		if (r1 == 0) and (r2 == 0):
			print "FB",
		elif r1 == 0:
			print "F",
		elif r2 == 0:
			print "B",
		else:
			print i,
			
	print

test_cases.close()
