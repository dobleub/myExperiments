#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ball_trajectory.py
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

import math as m

def frange3(start, end=None, inc=None):
    """A range function, that does accept float increments..."""

    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    if inc == None:
        inc = 1.0
    count = int(m.ceil((end - start) / inc))

    L = [None,] * count

    L[0] = start
    for i in xrange(1,count):
        L[i] = L[i-1] + inc
    return L
 
def drange(start, stop, step): 		# funcion generadora
	r = start
	while r < stop:
		yield r		# a;ade a la lista el nuevo numero valido
		r += step


def TrajectoryBall(v0,theta,x,y0):
	""" f(x)=xtanθ - 1/(2v2) * (gx2)/(cos2θ) + y0
		x = horizontal coordinate
		g = acceleration of gravity in m/s2
		v0 = velocity in km/h
		θ = angle in degrees
		y0 | 0 = initial position of the ball
		:. y = f(x)
	"""
	print "v0:",v0,"m/s"
	g = 9.81 # m/s2
	print """\
	v0 = %.1f km/h
	theta = %d degrees
	y0 = %.1f m
	x = %.1f m\
	""" % (v0, theta, x, y0)
	v0 = v0/3.6			# (3600s / 1h)(1km / 1000m) = 3.6 m/s
	theta = theta*m.pi/180
	
	y = x*m.tan(theta) - 1/(2*v0**2) * (g*x**2)/(m.cos(theta)**2) + y0
	print '	y = %.1f m' % y


def main():
	TrajectoryBall(15,60,0.5,1)
	return 0

if __name__ == '__main__':
	main()

