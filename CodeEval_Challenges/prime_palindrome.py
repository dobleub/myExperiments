#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0003. The biggest prime palindrome under 1000

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

cont=0
i = 1000
l = range(2,i)
while i > 1:
	np = nprimo(i,l)
	if np:
		np = list(str(np))
		npp = [n for n in np]
		npp.reverse()
		if np == npp:
			print i
			break
		else:
			next
	i-=1
