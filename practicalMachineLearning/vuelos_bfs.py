#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vuelos_bfs.py
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
# Vuelos con busqueda en amplitud

from arbol import Nodo

def buscarSolucionBfs(conexiones, estadoInicial, solucion):
	solucionado = False
	nodosVisitados = []
	nodosFrontera = []
	nodoInicial = Nodo(estadoInicial)
	nodosFrontera.append(nodoInicial)
	
	while (not solucionado) and len(nodosFrontera) != 0:
		nodo = nodosFrontera.pop(0)
		nodosVisitados.append(nodo)
		if nodo.getDatos() == solucion:
			solucionado = True
			return nodo
		else:
			# expandir nodos hijo (ciudades con conexion)
			datoNodo = nodo.getDatos()
			listaHijos = []
			for unHijo in conexiones[datoNodo]:
				hijo = Nodo(unHijo)
				listaHijos.append(hijo)
				if not hijo.enLista(nodosVisitados) and not hijo.enLista(nodosFrontera):
					nodosFrontera.append(hijo)
			nodo.setHijos(listaHijos)

def main():
	# code here
	conexiones = {
		'Malaga' : {'Salamanca', 'Madrid', 'Barcelona'},
		'Sevilla' : {'Santiago', 'Madrid'},
		'Granada' : {'Valencia'},
		'Valencia' : {'Barcelona'},
		'Madrid' : {'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'},
		'Salamanca' : {'Malaga', 'Madrid'},
		'Santiago' : {'Sevilla', 'Santander', 'Barcelona'},
		'Santander' : {'Santiago', 'Madrid'},
		'Zaragoza' : {'Barcelona'},
		'Barcelona' : {'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia'}
	}
	estadoInicial = 'Malaga'
	solucion = 'Santiago'
	nodoSolucion = buscarSolucionBfs(conexiones, estadoInicial, solucion)
	resultado = []
	nodo = nodoSolucion

	while nodo.getPadre() != None:
		resultado.append(nodo.getDatos())
		nodo = nodo.getPadre()
	resultado.append(estadoInicial)
	resultado.reverse()

	print(resultado)

if __name__ == '__main__':
	main()
