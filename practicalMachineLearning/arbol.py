#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arbol.py
#  
#  Copyright 2017 Edd Osorio <dobleub@debian>
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

class Nodo(object):
	"""Nodo implementation"""
	def __init__(self, datos, hijos=None):
		self.datos = datos
		self.hijos = None
		self.padre = None
		self.coste = None
		self.setHijos(hijos)

	def setHijos(self, hijos):
		self.hijos = hijos
		if self.hijos != None:
			for h in self.hijos:
				h.padre = self

	def getHijos(self):
		return self.hijos

	def setPadre(self, padre):
		self.padre = padre

	def getPadre(self):
		return self.padre

	def setDatos(self, datos):
		self.datos = datos

	def getDatos(self):
		return self.datos

	def setCoste(self, coste):
		self.coste = coste

	def getCoste(self):
		return self.coste

	def igual(self, nodo):
		if self.getDatos() == nodo.getDatos():
			return True
		else:
			return False

	def enLista(self, listaNodos):
		enLista = False
		for n in listaNodos:
			if self.igual(n):
				enLista = True
		return enLista

	def __str__(self):
		return str(self.getDatos())
