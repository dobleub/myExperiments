#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  carretera_ucs_uniformCostSearch.py
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
#  Viaje con carretera con Busqueda de coste uniforme

from arbol import Nodo

def compara(x, y):
	return x.getCoste() - y.getCoste()

def buscarSolucionUcs(conexiones, estadoInicial, solucion):
	solucionado = False
	nodosVisitados = []
	nodosFrontera = []
	nodoInicial = Nodo(estadoInicial)
	nodoInicial.setCoste(0)
	nodosFrontera.append(nodoInicial)

	while (not solucionado) and len(nodosFrontera) != 0:
		# ordenar la lista de nodos frontera
		nodosFrontera  = sorted(nodosFrontera, key=lambda n: n.getCoste())
		nodo = nodosFrontera.pop(0)
		# extraer nodo y a;adirlo a visitados
		nodosVisitados.append(nodo)
		if nodo.getDatos() == solucion:
			solucionado = True
			return nodo
		else:
			datoNodo = nodo.getDatos()
			listaHijos = []
			for unHijo in conexiones[datoNodo]:
				hijo = Nodo(unHijo)
				coste = conexiones[datoNodo][unHijo]
				hijo.setCoste(nodo.getCoste() + coste)
				listaHijos.append(hijo)

				if not hijo.enLista(nodosVisitados):
					# si esta el hijo en nodosFrontera
					if hijo.enLista(nodosFrontera):
						for n in nodosFrontera:
							if n.igual(hijo) and n.getCoste() > hijo.getCoste():
								nodosFrontera.remove(n)
								nodosFrontera.append(hijo)
					else:
						nodosFrontera.append(hijo)

			nodo.setHijos(listaHijos)



def main():
	# code here
	conexiones = {
		'Malaga' : {'Granada':125, 'Madrid':513},
		'Sevilla' : {'Madrid':514},
		'Granada' : {'Malaga':125, 'Madrid':423, 'Valencia':491},
		'Valencia' : {'Granada':491, 'Madrid':423, 'Zaragoza':309, 'Barcelona':346},
		'Madrid' : {'Salamanca':203, 'Sevilla':514, 'Malaga':513, 'Granada':423, 'Barcelona':603, 'Santander':437, 'Valencia':356, 'Zaragoza':313, 'Santiago':599},
		'Salamanca' : {'Santiago':390, 'Madrid':599},
		'Santiago' : {'Salamanca':390, 'Madrid':599},
		'Santander' : {'Madrid':437, 'Zaragoza':394},
		'Zaragoza' : {'Barcelona':296, 'Valencia':309, 'Madrid':313},
		'Barcelona' : {'Zaragoza':296, 'Madrid':603, 'Valencia':346}
	}
	estadoInicial = 'Malaga'
	solucion = 'Santiago'
	nodoSolucion = buscarSolucionUcs(conexiones, estadoInicial, solucion)
	nodo = nodoSolucion

	resultado = []
	while nodo.getPadre() != None:
		resultado.append(nodo.getDatos())
		nodo = nodo.getPadre()
	resultado.append(estadoInicial)
	resultado.reverse()

	print(resultado)
	print('Coste: ' + str(nodoSolucion.getCoste()))


if __name__ == '__main__':
	main()
