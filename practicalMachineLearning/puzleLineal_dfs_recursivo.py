#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  puzleLineal_dfs_recursivo.py
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
# Puzle lineal con busqueda en profuncidad recursiva

from arbol import Nodo

def buscarSolucionDfs_recursiva(nodoInicial, solucion, visitados):
	visitados.append(nodoInicial)
	if nodoInicial.getDatos() == solucion:
		return nodoInicial
	else:
		datoNodo = nodoInicial.getDatos()
		# operador izquierdo
		hijo = [datoNodo[1], datoNodo[0], datoNodo[2], datoNodo[3]]
		hijoIzquierdo = Nodo(hijo)
		# operados central
		hijo = [datoNodo[0], datoNodo[2], datoNodo[1], datoNodo[3]]
		hijoCentral = Nodo(hijo)
		#operador derecho
		hijo = [datoNodo[0], datoNodo[1], datoNodo[3], datoNodo[2]]
		hijoDerecho = Nodo(hijo)
		
		nodoInicial.setHijos([hijoIzquierdo, hijoCentral, hijoDerecho])

		for nodoHijo in nodoInicial.getHijos():
			if not nodoHijo.getDatos() in visitados:
				sol = buscarSolucionDfs_recursiva(nodoHijo, solucion, visitados)
				if sol != None:
					return sol

		return None

def main():
	# code here
	estadoInicial = [4,3,2,1]
	solucion = [1,2,3,4]
	nodoSolucion = None
	visitados = []
	nodoInicial = Nodo(estadoInicial)
	nodo = buscarSolucionDfs_recursiva(nodoInicial, solucion, visitados)

	resultado = []
	while nodo.getPadre() != None:
		resultado.append(nodo.getDatos())
		nodo = nodo.getPadre()
	resultado.append(estadoInicial)
	resultado.reverse()

	print(resultado)


if __name__ == '__main__':
	main()
