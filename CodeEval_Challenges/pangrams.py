#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0037 - Moderate. Pangrams

import sys
from string import join

test_cases = open(sys.argv[1], 'r')

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for test in test_cases:
	test.lower()
	l = list(test)
	ln = [s for s in abc if s not in l]
	
	if len(ln) == 0:
		print "NULL"
	else:
		print "".join(ln)
