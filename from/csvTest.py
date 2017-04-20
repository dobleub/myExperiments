#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  csvTest.py
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

import csv
from datetime import datetime

def main():
	path = 'google_stock_data.csv'
	file = open(path, newline='')
	
	# without csv module
	dataset = [line.strip().split(',') for line in open(path)]
	
	# with csv module
	reader = csv.reader(file)
	header = next(reader)
	# data = [row for row in reader]
	data = []
	for row in reader:
		# row = [date, open, high, low, close, volume, adj. close]
		date = datetime.strptime(row[0], '%m/%d/%Y')
		openPrice = float(row[1])
		high = float(row[2])
		low = float(row[3])
		close = float(row[4])
		volume = int(row[5])
		adjClose = float(row[6])
		
		data.append([date, openPrice, high, low, close, volume, adjClose])
		
	print(header)
	print(data[5])

if __name__ == '__main__':
    main()
