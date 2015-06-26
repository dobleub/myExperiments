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

import wx

class MyFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame with button', size=(300,100))
		panel = wx.Panel(self)			# Creating the panel
		button = wx.Button(panel, label='Close', pos=(125,10), size=(50,50))	# Adding the button to the panel
		self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)		# Binding the button click event
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)				# Binding the window close event
	
	def OnCloseMe(self, event):
		self.Close(True)
	
	def OnCloseWindow(self, event):
		self.Destroy()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MyFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
