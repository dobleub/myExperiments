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

ID_BUTTON1 = wx.NewId()
ID_BUTTON2 = wx.NewId()

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None, title="Event Propagation")
		self.SetTopWindow(self.frame)
		self.frame.Centre()
		self.frame.Show()
		
		self.Bind(wx.EVT_BUTTON, self.OnButtonApp)
		return True
	
	def OnButtonApp(self, event):
		event_id = event.GetId()
		if event_id == ID_BUTTON1:
			print "Button 1 event reached the App"
			
class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="MyFrame"):
		super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)
		# Attributes
		self.panel = wx.Panel(self)
		# Setup
		self.btn1 = wx.Button(self.panel, ID_BUTTON1, "Propagates")
		self.btn2 = wx.Button(self.panel, ID_BUTTON2, "Doesn't propagate")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.btn1, 0, wx.ALL, 10)
		sizer.Add(self.btn2, 0, wx.ALL, 10)
		self.panel.SetSizer(sizer)
		# Binding
		self.Bind(wx.EVT_BUTTON, self.OnButtonFrame)
	
	def OnButtonFrame(self, event):
		event_id = event.GetId()
		if event_id == ID_BUTTON1:
			print "Button 1 event reached the Frame"
			event.Skip()
		if event_id == ID_BUTTON2:
			print "Button 2 event reached the Frame"
			
class MyPanel(wx.Panel):
	def __init__(self, parent):
		super(MyPanel, self).__init__(parent)
		# Binding
		self.Bind(wx.EVT_BUTTON, self.OnPanelButton())
	
	def OnPanelButton(self, event):
		event_id = event.GetId()
		if event_id == ID_BUTTON1:
			print "Button 1 event reached the Panel"
			event.Skip()
		elif event_id == ID_BUTTON2:
			print "Button 2 event reached the Panel"
			# No skipping the event will cause its
			# propagation to end here


def main():
	app = MyApp(False)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()
