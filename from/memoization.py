#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memoization.py
#  
#  Copyright 2017 eosorio <eosorio@LAP-DES-222GC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import math
from functools import lru_cache

def isPrime(n):
	if n%2 == 0 and n > 2:
		return False
	return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))

fibonacci_cache = {}
def fibonacciMemoizationExplicit(n):
	if type(n) != int:
		raise TypeError('n must be a positive number');
	if n < 0:
		raise ValueError('n must be a positive number');
	
	# if we have a cacged value
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	
	# compute
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacciMemoizationExplicit(n-1) + fibonacciMemoizationExplicit(n-2)
	
	# cache de value
	fibonacci_cache[n] = value
	return value

@lru_cache(maxsize = 1000)
def fibonacciMemoizationTrivial(n):
	if type(n) != int:
		raise TypeError('n must be a positive number');
	if n < 0:
		raise ValueError('n must be a positive number');
		
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacciMemoizationTrivial(n-1) + fibonacciMemoizationTrivial(n-2)

def main(args):
	limit = 1001
	for n in range(1, limit):
		if(isPrime(n)):
			print(n, 'is prime')
	# print('-'*50)
	# for n in range(1, limit):
	# 	print(n, ':', fibonacciMemoizationExplicit(n))
	print('-'*50)
	for n in range(1, limit):
		print(n, ':', fibonacciMemoizationTrivial(n))
	

if __name__ == '__main__':
    sys.exit(main(sys.argv))
