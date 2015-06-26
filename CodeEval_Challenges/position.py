#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0019. Odd Numbers
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	line=test.split(",")
	nb=bin(int(line[0]))	
	nb=list(nb)
	nb.reverse()
	if nb[int(line[1])-1] == nb[int(line[2])-1]:
		print "true"
	else:
		print "false"
	
test_cases.close()
