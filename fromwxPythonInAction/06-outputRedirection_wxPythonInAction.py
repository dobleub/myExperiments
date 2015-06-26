#!/usr/bin/env python				
# -*- coding: utf-8 -*-
#
#  00_wx.py
#  
#  Copyright 2013 dobleub <blue.culture@live.com.mx>
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

""" Hello, wxPython program """

import wx
import sys

class MyFrame(wx.Frame):
		def __init__(self, parent, id, title):
			print 'Frame __init__'
			wx.Frame.__init__(self, parent, id, title)

class MyApp(wx.App):
	def __init__(self, redirect=True, filename=None):
		print 'App __init__'
		wx.App.__init__(self, redirect, filename)
	
	def OnInit(self):
		print 'OnInit'							# Writing to stdout
		self.frame = MyFrame(parent=None, id=-1, title='Startup') 	# Creating the Frame
		self.frame.Show()
		self.SetTopWindow(self.frame)
		print >> sys.stderr, 'Error message'	# Writing to stderr
		return True

	def OnExit(self):
		print 'OnExit'

if __name__ == '__main__':
	app = MyApp(redirect=True)		# Text redirection starts here
	print 'Before MainLoop'
	app.MainLoop()					# The main event loop is entered here
	print 'After MainLoop'
