#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  randomWalk.py
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

import random as r

def randomWalk(n):
	"""Return coordinates after n block random unit"""
	x = 0
	y = 0
	for i in range(n):
		step = r.choice(['N', 'S', 'E', 'O'])
		if step == 'N':
			y += 1
		elif step == 'S':
			y -= 1
		elif step == 'E':
			x += 1
		else:
			x -= 1
	return(x, y)

def randomWalkTwo(n):
	"""Return coordinates after n block random unit"""
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = r.choice([(0,1), (0,-1), (1,0), (-1,0)])
		x += dx
		y += dy
	return(x, y)
		
def main():
	for i in range(25):
		walk = randomWalkTwo(10)
		print(walk, 'Distance from home:', abs(walk[0] + walk[1]))
	
	# monte carlo
	nWalks = 5000
	for walkLenght in range(1, 31):
		noTransport = 0
		for i in range(nWalks):
			(x, y) = randomWalkTwo(walkLenght)
			distance = abs(x) + abs(y)
			if distance <= 4:
				noTransport += 1
		noTransportPercentaje = float(noTransport) / nWalks
		print('Walk size:', walkLenght, '/ % of no transport', 100*noTransportPercentaje)
	

if __name__ == '__main__':
    main()
