#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  puzleLineal_dfs_depthFirstSearch.py
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
# Puzle lineal con busqueda en profundidad

from arbol import Nodo

def buscarSolucionDfs(estadoInicial, solucion):
	solucionado = False
	nodosVisitados = []
	nodosFrontera = []
	nodoInicial = Nodo(estadoInicial)
	nodosFrontera.append(nodoInicial)

	while (not solucionado) and len(nodosFrontera) != 0:
		nodo = nodosFrontera.pop()
		nodosVisitados.append(nodo)
		if nodo.getDatos() == solucion:
			solucionado = True
			return nodo
		else:
			datoNodo = nodo.getDatos()
			# operador izquierdo
			hijo = [datoNodo[1], datoNodo[0], datoNodo[2], datoNodo[3]]
			hijoIzquierdo = Nodo(hijo)
			if not hijoIzquierdo.enLista(nodosVisitados) and not hijoIzquierdo.enLista(nodosFrontera):
				nodosFrontera.append(hijoIzquierdo)
			# operados central
			hijo = [datoNodo[0], datoNodo[2], datoNodo[1], datoNodo[3]]
			hijoCentral = Nodo(hijo)
			if not hijoCentral.enLista(nodosVisitados) and not hijoCentral.enLista(nodosFrontera):
				nodosFrontera.append(hijoCentral)
			#operador derecho
			hijo = [datoNodo[0], datoNodo[1], datoNodo[3], datoNodo[2]]
			hijoDerecho = Nodo(hijo)
			if not hijoDerecho.enLista(nodosVisitados) and not hijoDerecho.enLista(nodosFrontera):
				nodosFrontera.append(hijoDerecho)
			
			nodo.setHijos([hijoIzquierdo, hijoCentral, hijoDerecho])

def main():
	# code here
	estadoInicial = [4,2,3,1]
	solucion = [1,2,3,4]
	nodoSolucion = buscarSolucionDfs(estadoInicial, solucion)
	# mostrar resultado
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
