#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0004. Sum of the 1000 Prime numbers

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
l = range(2,10000)
j = i = 1
while True:
	np = nprimo(i,l)
	if np:
		cont += np
		if j < 1000:
			j+=1
		else:
			break
	i+=1

print cont
