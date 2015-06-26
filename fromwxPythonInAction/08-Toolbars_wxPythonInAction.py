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
#from PIL import Image
import images

class ToolbarFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Toolbars', size=(300,200))
		panel = wx.Panel(self)
		panel.SetBackgroundColour('White')
		statusBar = self.CreateStatusBar()		# Creating the status bar
		toolbar = self.CreateToolBar()			# Creating the toolbar
		toolbar.AddSimpleTool(wx.NewId(), images.GetNewBitmap(), 'New', "Long help for 'New'")	# Adding a tool to the bar
		toolbar.Realize()			# Preparing the toolbar to display
		menubar = wx.MenuBar()		# Creating a menu bar
		menu1 = wx.Menu()		# Creating 2 individual menus																																																																										`																																					
		menubar.Append(menu1, '&File')	# Item for menu1
		menu2 = wx.Menu()		#
		menu2.Append(wx.NewId(), '&Copy', 'Copy in Status bar')		# Adding 
		menu2.Append(wx.NewId(), 'C&ut', '')						# items
		menu2.Append(wx.NewId(), 'Paste', '')						# for
		menu2.AppendSeparator()										# menu2
		menu2.Append(wx.NewId(), 'Options...', 'Options in Status bar')
		menubar.Append(menu2, '&Edit')
		self.SetMenuBar(menubar)
		
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = ToolbarFrame(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
