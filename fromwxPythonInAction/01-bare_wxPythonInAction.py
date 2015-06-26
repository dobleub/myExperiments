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

#	This basic wxPython program illustrates the five basic steps you
#	must complete for every wxPython program you develop:


import wx				#		1 Import the necessary wxPython package

class App(wx.App):		#		2 Subclass the wxPython application class
	def OnInit(self):	#		3 Define an application initialization method
		frame = wx.Frame(parent=None, title='Bare')
		frame.Show()
		return True

app = App()				#		4 Create an application class instance
app.MainLoop()			#		5 Enter the application’s main event loop
