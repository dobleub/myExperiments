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
		self.frame = DropTargetFrame(None, title="Drag and Drop")
		
		self.SetTopWindow(self.frame)
		self.frame.Centre()
		self.frame.Show()
		return True

class FileAndTextDropTarget(wx.PyDropTarget):
	"""Drop target capable of accepting dropped
	files and text
	"""
	def __init__(self,file_callback,text_callback):
		assert callable(file_callback)
		assert callable(text_callback)
		super(FileAndTextDropTarget, self).__init__()
		# Atributtes
		self.fcallback = file_callback	# Drop file_callback
		self.tcallback = text_callback	# Drop text_callback
		self._data = None
		self.txtdo = None
		self.filedo = None
		# Setup
		self.InitObjects()
		
	def InitObjects(self):
		""" Inicialize text and file data objects """
		self._data = wx.DataObjectsComposite()
		self.txtdo = wx.TextDataObject()
		self.filedo = wx.FileDataObject()
		self._data.Add(self.txtdo, False)
		self._data.Add(self.filedo, True)
		self.SetDataObject(self._data)
		
	def OnData(self, x_cord, y_cord, drag_result):
		""" Called by the framework when data is dropped on the target """
		if self.GetData():
			data_format = self._data.GetReceivedFormat()
			if data_format.GetType() == wx.DF_FILENAME:
				self.fcallback(self.filedo.GetFilenames())
			else:
				self.tcallback(self.txtdo.GetText())
		return drag_result
		
class DropTargetFrame(wx.Frame):
	def __init_(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="DropTargetFrame"):
		super(DropTargetFrame, self).__init_(parent,id,pos,size,style,name)
		# Atributtes
		choises = ["Drag and Drop Text or files here",]
		self.list = wx.ListBox(self, choises=choises)
		self.dt = FileAndTextDropTarget(self.OnFileDrop, self.OnTextDrop)
		self.list.SetDropTarget(self.dt)
		# Setup
		self.CreateStatusBar()
		
	def OnFileDrop(self, files):
		self.PushStatusText("Files dropped")
		for f in files:
			self.list.Append(f)
	
	def OnTextDrop(self, text):
		self.PushStatusText("Text dropped")
		self.list.Append(text)
	
	
def main():
	app = MyApp(False)
	app.MainLoop()
	return 0

if __name__ == '__main__':
	main()

