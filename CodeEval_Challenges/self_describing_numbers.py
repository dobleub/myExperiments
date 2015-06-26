#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0040. Self Describing Numbers
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	l=test[:len(test)-1]
	l=map(int,l)
	w=len(l)
	
	l2=[]
	i=0
	while i < w:
		if l[i] < (w -1):
			if l[i] == l.count(i):
				l2.append(1)
			else:
				l2.append(0)
		else:
			l2.append(0)
		i+=1
	
	tmp = [1 for i in l2]
	if l2 == tmp:
		print 1
	else:
		print 0
	
test_cases.close()
