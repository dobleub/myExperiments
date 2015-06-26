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

# .../env python  				1 Shebang line

""" Spare.py is a starting point for wxPython program. """		# 	2 Docstring (documentation string)


import wx

class Frame(wx.Frame):			# 	3 Frame object
	pass
	
class App(wx.App):
	def OnInit(self):
		self.frame = Frame(parent=None, title='Spare')		#	4 Reference to the frame instance as an attribute of the application class instance
		self.frame.Show()
		self.SetTopWindow(self.frame)		# 	5 It’s an optional method that lets wxPython know which frame or dialog should be considered the main one

		return True

if __name__ == '__main__':		#	6 Test whether the module is being run as a program or was imported by another module

	app = App()
	app.MainLoop()
