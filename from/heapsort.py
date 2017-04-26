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
	_sortedItems = []
	
	# create the heap, this can be a tree, instead we use an array
	# child from k parent : 2k+1, 2k+2
	# parent from j child if j > 0 : (j-1/)2
	def __init__(self, itemsArray):
		for i in itemsArray:
			self._insertItem(i)
		print(self._items)

	def sort(self, inverted=False):
		i = 0
		self._sortedItems = []
		while len(self._items) > 0:
			self._sortedItems.append(self._extractItem())

		return self._sortedItems

	def _insertItem(self, item):
		self._items.append(item)
		idx = len(self._items)-1
		parentIdx = self._findItemParent(idx)
		while parentIdx >= 0:
			if self._items[parentIdx] > item:
				self._swap(parentIdx, idx)
			idx = parentIdx
			parentIdx = self._findItemParent(idx)

	def _extractItem(self):
		idx = 0
		item = self._items[idx]
		self._items[idx] = self._items[ len(self._items)-1 ]
		del self._items[ len(self._items)-1 ]
		while idx < len(self._items):
			childIdx = self._findParentChilds(idx)
			if childIdx[0] > 0 or childIdx[1] > 0:
				if childIdx[0] < childIdx[1]:
					if self._items[ childIdx[0] ] > self._items[ childIdx[1] ]:
						print(idx, childIdx[0], item, self._items[ childIdx[0] ])
						self._swap(idx, childIdx[0])
						idx = childIdx[0]
					else:
						print(idx, childIdx[1], item, self._items[ childIdx[1] ])
						self._swap(idx, childIdx[1])
						idx = childIdx[1]
				else:
					print(idx, childIdx[0], item, self._items[ childIdx[0] ])
					self._swap(idx, childIdx[0])
					idx = childIdx[0]
			else:
				break
			# idx += 1
		print(item, self._items)
		return item

	def _swap(self, x, y):
		tmp = self._items[x]
		self._items[x] = self._items[y]
		self._items[y] = tmp
		
	def _findItemParent(self, index):
		if index > 0:
			return int((index-1)/2)
		else:
			return -1

	def _findParentChilds(self, index):
		a, b = -1, -1 # child1, child2
		if ((index*2)+1) < len(self._items):
			a = (index*2)+1
		if ((index*2)+2) < len(self._items):
			b = (index*2)+2
		return a, b

def main():
	import random as r
	items = []
	for i in range(10):
		items.append(r.randint(100,9999))
	print(items)
	h = Heapsort(items)
	sortedItems = h.sort()
	print(sortedItems)

if __name__ == '__main__':
	main()
