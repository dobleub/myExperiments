#! /usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from math import sqrt
from random import randint, randrange
from myOwnFunctions import *

class MyPanel(wx.Panel):
	def __init__(self, *args, **kw):
		wx.Panel.__init__(self, *args, **kw)
		self.resizeNeeded = False
		#self.useGCDC = False
		#self.useBuffer = True
		
		# Definimos
		#self.SetBackgroundColour((51, 51, 51))
		self.SetBackgroundColour((120,120,120))
		self.SetForegroundColour((164, 211, 238))
		self.SetSize((640,480))
	
		# Eventos
		self.Bind(wx.EVT_SIZE, self.OnSize)
		#self.Bind(wx.EVT_IDLE, self.OnIdle)
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		
	def OnPaint(self, evt):	
		dc = wx.PaintDC(self) # Define el contenedor
		dc.Clear()
	
		dc.BeginDrawing()
		dc.SetPen(wx.Pen(self.GetForegroundColour(),1))
		#dc.SetBrush(wx.Brush(self.GetBackgroundColour()))
		dc.SetBrush(wx.Brush(self.GetForegroundColour()))
		
		titulo = "PLANO CARTESIANO"
		(w,h) = dc.GetTextExtent(titulo)
		(x,y) = self.GetSize()
		dc.DrawText(titulo, ((x/2)-(w/2) - 100), 20)
	
		# Dibujar Origen Plano Cartesiano
		dc.DrawLine(0,(y/2),x,(y/2)) # X
		dc.DrawLine((x/2),0,(x/2),y) # Y
		dc.DrawText("x", (x-15), (y/2)-3)
		dc.DrawText("y", (x/2)+3, 5)
		origen = [(x/2),(y/2)]
		dc.DrawCircle(int(origen[0]), int(origen[1]),2)
		
		# Definimos funciones
		
		
		# Problema 3 - Funcion random
		i=0
		while i < 100:
			rnd0 = randrange(-200,200,5)
			rnd1 = randrange(-200,200,5)
			#rnd = randint(0,100)
			dc.DrawCircle((origen[0]+rnd0),(origen[1]-rnd1),2)
			#dc.DrawText(str(rnd0)+","+str(rnd1),(origen[0]+rnd0),(origen[1]-rnd1))
			i+=1
		
		
		dc.EndDrawing()
	
	def OnSize(self, evt):
		self.resizeNeeded = True
	
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None, title="None")
		self.draw_panel = MyPanel(self)
		
		panelSizer = wx.BoxSizer(wx.VERTICAL)
		panelSizer.Add(self.draw_panel,0,wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,5)
		self.SetSizer(panelSizer)
		panelSizer.Fit(self)
		self.Show()
		
	def AppClear():
		self.draw_panel.Clear()
	
	resize_delay = 300	
	def TriggerResize(self, size):
		self.resize(size, self.resize_delay)
		self.resize_delay = 100
	
	def TriggerRedraw(self):
		self.repaint(10)
		

## MAIN
if __name__=="__main__":
	app = wx.App(False)
	MyFrame()
	app.MainLoop()
