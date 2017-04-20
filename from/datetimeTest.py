#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datetime.py
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

def main():
	import datetime as d
	gvr = d.date(1956, 1, 31)
	test = d.datetime(2017, 4, 20, 12, 14, 30)
	print(gvr)
	print(gvr.year, gvr.month, gvr.day)
	print(test)
	
	
if __name__ == '__main__':
    main()
