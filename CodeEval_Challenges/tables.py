#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0023. Multiplication Tables

l = range(1,13)
ln = []
for i in l:
	for j in l:
		r = j * i
		if len(str(r)) == 1:
			ln.append("   "+str(r))
		elif len(str(r)) == 2:
			ln.append("  "+str(r))
		else:
			ln.append(" "+str(r)) 
			
	print str("".join(ln))
	ln = []
