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

class Frame(wx.Frame):
	""" Frame class that display an image """
	def __init__(self, image, parent=None, id = -1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
		""" Create a frame instance and display image """
		temp = image.ConvertToBitmap()
		size = image.GetWidth(), image.GetHeight()
		wx.Frame.__init__(self, parent, id, title, pos, size)
		self.bmp = wx.StaticBitmap(parent = self, bitmap=temp)
	
class App(wx.App):
	""" Aplication class """
	def OnInit(self):
		image = wx.Image('Pepper_Portrait_by_Artgerm.jpg', wx.BITMAP_TYPE_JPEG)
		self.frame = Frame(image)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

def main():
	app = App()
	app.MainLoop()
	
if __name__ == '__main__':
	main()
