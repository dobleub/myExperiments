#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0025. Odd Numbers
import sys
l=range(1,100)
m=[n for n in l if n % 2 != 0]

for i in m:
	print i
