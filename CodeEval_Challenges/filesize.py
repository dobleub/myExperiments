#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 0026. File size in bytes
import sys
from os import path

test_cases = open(sys.argv[1], 'r')

print path.getsize(sys.argv[1])
	
test_cases.close()
