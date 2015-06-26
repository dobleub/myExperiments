#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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

class MyApp(wx.App):
	def OnInit(self):
		self.frame=MyFrame(None, title='Handlers Exp01')
		self.SetTopWindow(self.frame)
		self.frame.Show()
		return True
		
class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="MyFrame"):
		super(MyFrame, self).__init__(parent,id,title,pos,size,style,name)
		
		self.panel=wx.Panel(self)		# Attributes
		self.panel.SetBackgroundColour(wx.BLACK)
		button = wx.Button(self.panel, label='Get children', pos=(50,50))
		self.btnId = button.GetId()
		self.Bind(wx.EVT_BUTTON, self.OnButton, button)		# Event Handlers
	
	def OnButton(self,event):
		"""Called when the button is Clicked"""
		print '\nFrame Children: '
		for child in self.GetChildren():
			print "%s" % repr(child)
		
		print '\nPanel FindWindowById: '
		button = self.panel.FindWindowById(self.btnId)
		print "%s" % repr(button)
		button.SetLabel("Changed Label")			# Change the Button's label
		
		print '\nButton GetParent: '
		panel = button.GetParent()
		print "%s" % repr(panel)
		
		print '\nGet the App Object: '
		app = wx.GetApp()
		print "%s" % repr(app)
		
		print '\nGet the Frame from the App: '
		frame = app.GetTopWindow()
		print "%s" % repr(frame)


def main():
	app = MyApp(False)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()

