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

class MyApp(wx.App):
	def OnInit(self):
		frame = MyFrame("Hello World", (50, 60), (450, 340))
		frame.Show()
		self.SetTopWindow(frame)
		return True
		
class MyFrame(wx.Frame):
	def __init__(self, title, pos, size):
		wx.Frame.__init__(self, None, -1, title, pos, size)
		menuFile = wx.Menu()
		menuFile.Append(1, "&About...")
		menuFile.AppendSeparator()
		menuFile.Append(2, "E&xit")
		menuBar = wx.MenuBar()
		menuBar.Append(menuFile, "&File")
		self.SetMenuBar(menuBar)
		self.CreateStatusBar()
		self.SetStatusText("Welcome to wxPython!")
		self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
		self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
		
	def OnQuit(self, event):
		self.Close()
	
	def OnAbout(self, event):
		wx.MessageBox("This is a wxPython Hello world sample", "About Hello World", wx.OK | wx.ICON_INFORMATION, self)
		
if __name__ == '__main__':
	app = MyApp(False)
	app.MainLoop()
