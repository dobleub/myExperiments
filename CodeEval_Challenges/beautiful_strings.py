#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0083. Beautiful Strings

import sys
from string import lower

test_cases = open(sys.argv[1], 'r')

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for test in test_cases:
	m = len(test)-1
	l = list(test[:m])
	l1 = [s for s in l if s != " "]
	l1 = map(lower,l1)
	l2 = []
	[l2.append(s) for s in l1 if s not in l2 and s in abc]
	c = []
	[c.append(l1.count(i)) for i in l2]
	c.sort()
	c.reverse()
	s = []
	j=27
	for i in c:
		if j > 0:
			j-=1
		else:
			j = 1
		s.append(i * j)
	
	print sum(s)
