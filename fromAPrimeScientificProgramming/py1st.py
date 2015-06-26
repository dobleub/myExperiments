#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  py1st.py
#  
#  Copyright 2014 dobleub <dobleub@MARY-LAPTOP>
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

import math

def frange3(start, end=None, inc=None):
    """A range function, that does accept float increments..."""

    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    if inc == None:
        inc = 1.0
    count = int(math.ceil((end - start) / inc))

    L = [None,] * count

    L[0] = start
    for i in xrange(1,count):
        L[i] = L[i-1] + inc
    return L
 
def drange(start, stop, step): 		# fundion generadora
	r = start
	while r < stop:
		yield r		# a;ade a la lista el nuevo numero valido
		r += step



def VerticalMotion(v0):
	""" y(t)=v0t-1/2gt2
		v0 = initial velocity
		t = time
		g = acceleration of gravity
		v0t-1/2gt2 = t(v0-1/2gt) => t=0 | t = 2v0g
	"""
	print "v0:",v0,"m/s"
	g = 9.81 # m/s2
	t = (2*v0)/g
	#rango = [x * 0.1 for x in range(0, int(t*10))]
	rango = frange3(0,t,0.1)
	l=[]
	for x in rango:
		#l.append((v0 * x)-(0.5 * g * x**2))
		print x ,"s"," ",(v0 * x)-(0.5 * g * x**2),"m"
	#print ",".join(l)

def main():
	VerticalMotion(5)
	return 0

if __name__ == '__main__':
	main()

