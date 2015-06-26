#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0046. Sum of Prime numbers

import sys
from string import join
#import time

test_cases = open(sys.argv[1], 'r')

def nprimo(n,l):
	if n == 1:
		return False
	elif n == 2:
		return n
	else:
		for i in l:
			if n % i == 0:
				return False
				break
			else:
				if i == (n - 1):
					return n

for test in test_cases:
	#t0 = time.time()
	a = test[:len(test)-1]
	a = int(a)
	
	lnp=[]
	l = range(2,a)
	j = i = 1
	while i < a:
		np = nprimo(i,l)
		if np:
			lnp.append(str(np))
		i += 1
	
	print ",".join(lnp)#, time.time() - t0
	
test_cases.close()
