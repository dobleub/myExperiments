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

class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="MyFrame"):
		super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)
		# Attributes
		self.panel = wx.Panel(self)
		# Setup
		self.btn1 = wx.Button(self.panel, label="Push me")
		self.btn2 = wx.Button(self.panel, label="Push me too")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.btn1, 0, wx.ALL, 10)
		sizer.Add(self.btn2, 0, wx.ALL, 10)
		self.panel.SetSizer(sizer)
		# Binding
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.btn1)
		self.Bind(wx.EVT_BUTTON, lambda event: self.btn1.Enable(not self.btn1.Enabled), self.btn2)
		
	def OnButton(self, event):
		""" Called when self.btn1 is clicked """
		event_id = event.GetId()
		event_obj = event.GetEventObject()
		print "Button 1 Clicked: "
		print "Id= %d" % event_id
		print "Object= %s" % event_obj.GetLabel()

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None, title="Handling events")
		self.SetTopWindow(self.frame)
		
		self.frame.Centre()
		self.frame.Show()
		return True

def main():
	app = MyApp(None)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()

