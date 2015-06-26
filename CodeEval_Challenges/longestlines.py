#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0002 - Moderate. Longest Lines

import sys
from string import join

test_cases = open(sys.argv[1], 'r')
cad = []
for test in test_cases:
	l = len(test) - 1
	try:
		n = int(test[:l])
	except:
		line = list(test[:l])
		cad.append(line)
		#print "".join(line)
l = []
for i in cad:
	l.append(len(i))
l.sort()
l.reverse()
i = 0
while i < n:
	for j in cad:
		if len(j) == l[i]:
			print "".join(j)
	i += 1
