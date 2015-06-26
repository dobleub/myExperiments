#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NFOne.py
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
import time

def verificar_primo(numero):
	rango = range(2,numero)
	if numero == 1:
		return False
	elif numero == 2:
		return numero
	else:
		for elementos in rango:
			if numero % elementos == 0:
				return False
				break
			else:
				if elementos == numero - 1:
					return numero

def main():
	t0 = time.time()
	archivo = open("NFOne.txt","w+")
	i=100
	
	while i < 9999:
		c=c1=0
		if i < 1000:
			s = "0" + str(i)
		else:
			s = str(i)
		
		for e in s:
			c += s.count(e)
			c -= 1
			c1 += s.count(str(int(e)+1))
			
		if c == 0 and c1==0:
			#archivo.write("%s\t%i\n" % (s,c1))
			if verificar_primo(int(s)):
				archivo.write("%s\n" % s)
		i+=1
	
	archivo.write("%s" % (time.time() - t0))
	
	archivo.close()
	return 0

if __name__ == '__main__':
	main()
