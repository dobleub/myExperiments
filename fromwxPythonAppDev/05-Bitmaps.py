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

import os
import wx

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None,title="Bitmaps")
		self.SetTopWindow(self.frame)
		self.frame.Centre()		# Centra la App
		self.frame.Show()
		return True
	
class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="myframe"):
		super(MyFrame,self).__init__(parent,id,title,pos,size,style,name)
		
		self.panel=wx.Panel(self)
		
		#img_path = os.path.abspath("Pepper_Portrait_by_Artgerm.jpg")
		img_path = os.path.abspath("render_by_katkoyox-min.png")
		#bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_JPEG)
		bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_PNG)
		self.bitmap = wx.StaticBitmap(self.panel,bitmap=bitmap)

def main():
	app = MyApp(False)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()

