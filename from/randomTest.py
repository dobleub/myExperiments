#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  randomTest.py
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

import random

# random numbers from interval [3, 7]
def rndInterval():
	# random > scale > shift > return
	return (4 * random.random()) + 3

def main():
	limit = 10
	for i in range(limit):
		print(rndInterval())
	print(20*'-')
	for i in range(limit):
		print(random.uniform(3,7))
	print(20*'-')
	for i in range(limit):
		# average, sigma
		print(random.normalvariate(5,0.2))
	print(20*'-')
	outcome = ['stone', 'papel', 'scissors']
	for i in range(20):
		print(random.choice(outcome))
	

if __name__ == '__main__':
    main()
