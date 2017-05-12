#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vuelos_bpi_busquedaProfundidadIterativa.py
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
# Vuelos con busqueda con profundidad iterativa

from arbol import Nodo

def Dfs_bpi(conexiones, nodo, solucion):
	for limite in range(0,100):
		visitados = []
		sol = buscarSolucionDfs_recursive(conexiones, nodo, solucion, visitados, limite)
		if sol != None:
			return sol

def buscarSolucionDfs_recursive(conexiones, nodo, solucion, visitados, limite):
	if limite > 0:
		visitados.append(nodo)
		if nodo.getDatos() == solucion:
			return nodo
		else:
			datoNodo = nodo.getDatos()
			listaHijos = []
			for unHijo in conexiones[datoNodo]:
				hijo = Nodo(unHijo)
				if not hijo.enLista(visitados):
					listaHijos.append(hijo)

			nodo.setHijos(listaHijos)

			for nodoHijo in nodo.getHijos():
				if not nodoHijo.getDatos() in visitados:
					sol = buscarSolucionDfs_recursive(conexiones, nodoHijo, solucion, visitados, limite-1)
					if sol != None:
						return sol

		return None


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
	nodoInicial = Nodo(estadoInicial)
	nodo = Dfs_bpi(conexiones, nodoInicial, solucion)
	
	if nodo != None:
		resultado = []
		while nodo.getPadre() != None:
			resultado.append(nodo.getDatos())
			nodo = nodo.getPadre()
		resultado.append(estadoInicial)
		resultado.reverse()

		print(resultado)
	else:
		print('Solucion no encontrada')

if __name__ == '__main__':
	main()
