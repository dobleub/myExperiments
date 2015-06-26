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
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "My Frame", size=(300,300))
		panel = wx.Panel(self,-1)
		panel.Bind(wx.EVT_MOTION, self.OnMove)
		wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
		self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))

		
	def OnMove(self, event):
		pos = event.GetPosition()
		self.posCtrl.SetValue("%s, %s" % (pos.x,pos.y))

def main():
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show(True)
	app.MainLoop()
	

if __name__ == '__main__':
	main()
