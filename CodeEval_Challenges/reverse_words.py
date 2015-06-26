#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0008. Reverse Words
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	line=test.split()
	line.reverse()
	for i in line:
		print i,
			
	print

test_cases.close()
