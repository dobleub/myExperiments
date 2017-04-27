#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  heapsort.py
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

class Heapsort:
	_items = []
	
	# create the heap, this can be a tree, instead we use an array
	# child from k parent : 2k+1, 2k+2
	# parent from j child if j > 0 : (j-1/)2
	def __init__(self, itemsArray):
		self._items = itemsArray

	def sort(self, inverted=False):
		i = 0
		end = len(self._items)
		start = end // 2 - 1 # use // instead of /
		for i in range(start, -1, -1):
			self._heapify(end, i)
		for i in range(end-1, 0, -1):
			self._swap(i, 0)
			self._heapify(i, 0)

		return self._items

	def _heapify(self, end,i):
		l = 2 * i + 1
		r = 2 * i + 2
		max = i
		if l < end and self._items[i] < self._items[l]:
			max = l
		if r < end and self._items[max] < self._items[r]:
			max = r
		if max != i:
			self._swap(i, max)
			self._heapify(end, max)

	def _swap(self, x, y):
		tmp = self._items[x]
		self._items[x] = self._items[y]
		self._items[y] = tmp

def main():
	import random as r
	items = []
	for i in range(20):
		items.append(r.randint(-1000,1000))
	print(items)
	h = Heapsort(items)
	sortedItems = h.sort()
	print(sortedItems)

if __name__ == '__main__':
	main()
