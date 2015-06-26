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
	def __init__(self, parent, *args, **kwargs):
		super(MyFrame, self).__init__(parent, *args, **kwargs)
		# Attibutes
		self.panel = wx.Panel(self)
		self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
		# Layout
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.txtctrl, 1, wx.EXPAND)
		self.panel.SetSizer(sizer)
		self.CreateStatusBar() # For output display
		# Event Handlers
		self.txtctrl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		self.txtctrl.Bind(wx.EVT_CHAR, self.OnChar)
		self.txtctrl.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
	
	def OnKeyDown(self, event):
		""" OnKeyDown event is the first """
		print "OnKeyDown called"
			# Get information about the event and log it to the Status Bar for Display
		key_code = event.GetKeyCode()
		raw_code = event.GetRawKeyCode()
		modifiers = event.GetModifiers()
		msg = "Key: %d, Raw: %d, Modifiers: %d" % (key_code, raw_code, modifiers)
		print msg
			# Must Skip the event to allow OnChar to be called 
		event.Skip()
	
	def OnChar(self, event):
		""" The OnChar event comes second and is where the character associated with the key is put into the control   """
		print "OnChar called"
		modifiers = event.GetModifiers()
		key_code = event.GetKeyCode()
		# Beep at the user whe the Shift key is down and disallow input
		if modifiers & wx.MOD_SHIFT:
			wx.Bell()
		elif chr(key_code) in 'aeiou':
			# When the vowel is pressed append a question mark at the end
			self.txtctrl.AppendText('?')
		else:
			# Let the text go in to the buffer
			event.Skip()
		
	def OnKeyUp(self, event):
		""" OnKeyUp come last """
		print "OnKeyUp called"
		event.Skip()
		
		
class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None)
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

