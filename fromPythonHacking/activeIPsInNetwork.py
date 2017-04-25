#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  activeIPsInNetwork.py
#  
#  Copyright 2017 Edd Osorio <dobleub@debian>
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

from subprocess import Popen, PIPE

def main():
	for ip in range(1,256):
		currentIP = '192.168.0.' + str(ip)
		subprocess = Popen(['/bin/ping', '-c 1', currentIP], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stdout, stdin = subprocess.communicate(input=None)
		if 'bytes from ' in stdout:
			print stdout
			print 'IP ' + currentIP + '\n'
		
	return 0

if __name__ == '__main__':
	main()

