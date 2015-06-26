#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 dobleub <blue.culture@live.com.mx>
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

class MyPanel(wx.Panel):
	def __init__(self, parent):
		super(MyPanel, self).__init__(parent)
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
	
	def AddChild(self, child):
		sizer = self.GetSizer()
		sizer.Add(child, 0, wx.ALIGN_LEFT|wx.ALL, 8)
		return super(MyPanel, self).AddChild(child)
	
class MyVirtualPanel(wx.PyPanel):
	def __init__(self, parent):
		super(MyVirtualPanel, self).__init__(parent)
		sizer = wx.BoxSizer()
		self.SetSizer(sizer)
		
	def AddChild(self, child):
		sizer = self.GetSizer()
		sizer.Add(child, 0 , wx.ALIGN_LEFT|wx.ALL, 8)
		return super(MyVirtualPanel, self).AddChild(child)

class MyFrame(wx.Frame):
	def __init__(self, parent, *args, **kwargs):
		super(MyFrame, self).__init__(parent, *args, **kwargs)
		# Atributtes
		self.mypanel = MyPanel(self)
		self.mypanel.SetBackgroundColour(wx.BLACK)
		self.virtpanel = MyVirtualPanel(self)
		self.virtpanel.SetBackgroundColour(wx.WHITE)
		# Setup
		self.__DoLayout()
	
	def __DoLayout(self):
		""" Layout the Window """
		# Layout the controls using a sizer
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.mypanel, 1, wx.EXPAND)
		sizer.Add(self.virtpanel, 1, wx.EXPAND)
		self.SetSizer(sizer)
		# Create 3 children for the top panel
		for x in range(3):
			wx.Button(self.mypanel, label="My panel %d" % x)
		# Create 3 children for the top panel
		for x in range(3):
			wx.Button(self.virtpanel, label="Virtual Panel %d" % x)
		
		self.SetInitialSize(size=(300,200))
	
class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None, title="Virtualized Methods")
		self.SetTopWindow(self.frame)
		
		self.frame.Centre()
		self.frame.Show()
		return True

def main():
	app = MyApp(False)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()

