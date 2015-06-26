#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Primeras pruebas: Programas sencillos

# a) Escribir un programa que le pregunte al usuario una cantidad de pesos, tasa de interes y a;os y mostrar el resultado
# 	 en base a Cn = C * (1 + x/100)^n .: C = capital inicial, x = tasa de interes, n = numero de a;os
def porcentaje_interes():
	capital = float(raw_input("capital inicial: $"))
	tasa = float(raw_input("tasa de interes: "))
	anios = float(raw_input("a;os: "))
	print "Monto final :", (capital * pow((1 + tasa/100),anios))

# b) Factorial de un numero
def faq(numero):
	if numero == 0:
		print 1
		return 1
	else:
		numero = numero * faq(numero -1)
		print numero
		return numero
	
def factorial():
	numero = int(raw_input("numero: "))
	faq(numero)

# c) Imprimir fichas de domino
def rellena(dots):
	dot = [["*"]]
	zero= [["0"]]
	if dots % 2.0 == 0:
		line = [a * 2 for a in dot] * (dots/2)
	else:
		line = [a * 2 for a in dot] * (dots/2)
		line.append(["*","0"])
	
	if (dots/2.0) < 0.5:
		line = [b * 2 for b in zero] * 3
	elif (dots/2.0) < 1.5:
		line.append(["0","0"])
		line.append(["0","0"])
	elif (dots/2.0) < 2.5:
		line.append(["0","0"])

	for i in line:
		print "| ",
		for j in i:
			if j == "0":
				print "   ",
			else:
				print j, " ",
		print "|"

def print_ficha(up,sub):
	print " ----------"
	rellena(up)
	print "|----------|"
	rellena(sub)
	print " ---------- \n"

def fichas_domino():
	i=j=0
	while True:
		while True:
			print_ficha(i,j)
			if j == 6:
				break
			j+=1
		j=0
		if i == 6:
			break
		i+=1

# d) Calcular catidad de segundos en un tiempo dado en hh:mm:ss y viceversa
def calcular_segundos():
	hora = raw_input("hora en formato hh:mm:ss -: ")
	aux = hora.split(":")
	hValida = 0
	try:
		for i in aux:
			if int(i) > 60:
				hValida += 1
		
		if hValida == 0:
			print "La hora ", hora, " tiene ", ((int(aux[0]) * 3600) + (int(aux[1]) * 60) + int((aux[2]))), " segundos"
		else:
			print "La hora no se puede procesar"
			
	except:
		print "La hora no se puede procesar"

def calcular_horas(segs):
	#segs = raw_input("segundos: ")
	try:
		segs = int(segs)
		print segs, "segundos son ", (segs/3600),":",((segs%3600)/60),":",((segs%3600)%60)," horas"
	except:
		print "La hora no se puede procesar"
		
# e) Sumar horas
def sumar_horas():
	hora0 = raw_input("hora en formato hh:mm:ss -: ")
	hora1 = raw_input("hora en formato hh:mm:ss -: ")
	aux0 = hora0.split(":")
	aux1 = hora1.split(":")

	hValida0 = 0
	hValida1 = 0
	try:
		for i in aux0:
			if int(i) > 60:
				hValida0 += 1
		for j in aux1:
			if int(j) > 60:
				hValida1 += 1
		
		if hValida0 == 0 and hValida1 == 0:
			segs = ((int(aux0[0]) + int(aux1[0]))  * 3600) + ((int(aux0[1]) + int(aux1[1])) * 60) + (int(aux0[2]) + int(aux1[2]))
			calcular_horas(segs)
		else:
			print "La hora no se puede procesar"
			
	except:
		print "La hora no se puede procesar"

# f) Dado un vector al origen (definido por (x,y)) devuelva la norma del vector dado por ||x,y||= sqrt(x^2,y^2)
import wx
from math import sqrt
from random import randint, randrange

class MyPanel(wx.Panel):
	def __init__(self, *args, **kw):
		wx.Panel.__init__(self, *args, **kw)
		self.resizeNeeded = False
		#self.useGCDC = False
		#self.useBuffer = True
		
		# Definimos
		self.SetBackgroundColour((51, 51, 51))
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
	
		# Ahora si empezamos con en problema 1
		#dc.SetPen(wx.Pen(self.GetBackgroundColour(),1))
		#xx = 40			# corrdenadas x,y del punto del triangulo, esperemos que luego se haga dinamico
		#yy = 80
		#cX = int(origen[0])+ xx
		#cY = int(origen[1]) - yy
		#dc.DrawCircle(cX,cY,2)
		#dc.DrawLine(int(origen[0]),int(origen[1]),cX,cY)				# Hipotenusa
		#dc.DrawLine(int(origen[0]),int(origen[1]),cX,int(origen[1]))	# Cateto 1
		#dc.DrawLine(cX,int(origen[1]),cX,cY)							# Cateto 2
	
		#hipotenusa = "h: " + '%6.3f' % ( sqrt(pow(xx,2) + pow(yy,2)) )
		#dc.DrawText(hipotenusa, int(origen[0])+(xx/2)-65, int(origen[1])-(yy/2)-10)
		#if xx < yy:
			#co = "co: " + '%6.2f' % ( xx )
			#ca = "ca: " + '%6.2f' % ( yy )
		#else:
			#ca = "co: " + '%6.2f' % ( xx )
			#co = "ca: " + '%6.2f' % ( yy )
		#dc.DrawText(co, cX-(xx/2)-20, int(origen[1]))
		#dc.DrawText(ca, cX+5, cY+(yy/2))
		
		# Prolema 1.5 - Distancia entre dos puntos
		def distancia(x1,y1,x2,y2):
			d = sqrt(((x2-x1)**2) + ((y2-y1)**2))
			return "d: " + '%6.3f' % (d)
		
		xx1 = 89
		yy1 = 34
		xx2 = 100
		yy2 = 129
		
		x1 = int(origen[0]) + xx1
		y1 = int(origen[1]) - yy1
		x2 = int(origen[0]) + xx2
		y2 = int(origen[1]) - yy2
		
		dc.DrawLine(x1,y1,x2,y2)
		txt = distancia(xx1,yy1,xx2,yy2)
		dc.DrawText( txt,int(origen[0])+((xx2-xx1)),int(origen[1]-((yy2-yy1))) )
		
		dc.DrawCircle(x1,y1,2)
		p2 = str(xx1) + "," + str(yy1)
		dc.DrawText(p2,x1,y1)
		
		dc.DrawCircle(x2,y2,2)
		p3 = str(xx2) + "," + str(yy2)
		dc.DrawText(p3,x2,y2)
		
		dc.SetBrush(wx.Brush("BLUE"))
		dc.DrawCircle( (int(origen[0])+sqrt((xx1**2)+(yy1**2)) ), ( int(origen[1])-sqrt((xx2**2) + (yy2**2)) ),2)
		
		# Problema 3 - Funcion random
		#i=0
		#while i < 100:
			#rnd0 = randrange(-200,200,5)
			#rnd1 = randrange(-200,200,5)
			##rnd = randint(0,100)
			#dc.DrawCircle((origen[0]+rnd0),(origen[1]-rnd1),2)
			##dc.DrawText(str(rnd0)+","+str(rnd1),(origen[0]+rnd0),(origen[1]-rnd1))
			#i+=1
		
		
		
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
		

def CallMyApp():
	app = wx.App(False)
	MyFrame()
	app.MainLoop()


# g) Una funcion recursiva
def cuenta_atras(n):
	if n == 0:
		print "Despegando!"
	else:
		print n
		cuenta_atras(n-1)

def call_CA():
	num = input("numero: ")
	cuenta_atras(num)

# h) calcular el modulo de una division
def modulo_div():
	numero1 = int(raw_input("numero: "))
	numero2 = int(raw_input("numero: "))
	cociente = numero1 / numero2
	residuo = (cociente * numero2) - numero1
	
	print abs(residuo)
	


## MAIN
if __name__=="__main__":
	CallMyApp()
	
	
	
