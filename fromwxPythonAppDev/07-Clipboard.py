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
#  How to set/get data from Clipoard
#  Data types:
#		TextDataObject()
#		BitmapDataObject()
#		CustomDataObject()
#		DataObjectComposite()
#		FileDataObject()
#		URLDataObject()

def SetClipboardText(text):
	""" Put text in the clipboard
	@param text: string
	"""
	data_o = wx.TextDataObject()
	data_o.SetText(text)
	if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
		wx.TheClipboard.SetData(data_o)
		wx.TheClipboard.Close()
	
def GetClipboardText():
	""" Get text from cipboard
	@param text: string
	"""
	text_obj = wx.TextDataObject()
	rtext = ""
	if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
		if wx.TheClipboard.GetData(text_obj):
			rtext = text_obj.GetText()
		wx.TheClipboard.Close()
		return rtext
