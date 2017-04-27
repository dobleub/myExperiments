#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3SAT - geneticAlgorithm.py
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

import math as m
import random as r

def poblacion_inicial(max_poblacion, num_vars):
	"""Crear poblacion inicial aleatoria"""
	poblacion = []
	for i in range(max_poblacion):
		gen = []
		for i in range(num_vars):
			if r.random() > 0.5:
				gen.append(1)
			else:
				gen.append(0)
		poblacion.append(gen)

	return poblacion

def adaptacion_3sat(gen, solucion):
	"""Contar clausúlas correctas"""
	n = 3
	cont = 0
	clausula_ok = True
	for i in range(len(gen)):
		n -= 1
		if gen[i] != solucion[i]:
			clausula_ok = False
		if n == 0:
			if clausula_ok:
				cont += 1
			n = 3
			clausula_ok = True
	if n > 0:
		if clausula_ok:
			cont += 1

	return cont

def evalua_poblacion(poblacion, solucion):
	"""Evalúa todos los genes de la pobalción"""
	adaptacion = []
	for i in range(len(poblacion)):
		adaptacion.append(adaptacion_3sat(poblacion[i], solucion))

	return adaptacion

def seleccion(poblacion, solucion):
	"""Selecciona los genes seleccionados"""
	adaptacion = evalua_poblacion(poblacion, solucion)
	# suma de todas las puntuaciones
	total = 0
	for i in range(len(adaptacion)):
		total += adaptacion[i]
	# escogemos dos elementos
	val1 = r.randint(0, total)
	val2 = r.randint(0, total)
	sum_sel = 0
	for i in range(len(adaptacion)):
		sum_sel += adaptacion[i]
		if sum_sel >= val1:
			gen1 = poblacion[i]
			break
	sum_sel = 0
	for i in range(len(adaptacion)):
		sum_sel += adaptacion[i]
		if sum_sel >= val2:
			gen2 = poblacion[i]
			break

	return gen1, gen2

def cruce(gen1, gen2):
	"""Cruza 2 genes y retorna 2 descendientes"""
	nuevo_gen1 = []
	nuevo_gen2 = []
	corte = r.randint(0, len(gen1))
	nuevo_gen1[0:corte] = gen1[0:corte]
	nuevo_gen1[corte:] = gen2[corte:]
	nuevo_gen2[0:corte] = gen2[0:corte]
	nuevo_gen2[corte:] = gen1[corte:]

	return nuevo_gen1, nuevo_gen2

def mutacion(prob, gen):
	"""Muta un gen con una probabilidad prob"""
	if r.random() < prob:
		cromosoma = r.randint(0, len(gen)-1)
		if gen[cromosoma] == 0:
			gen[cromosoma] = 1
		else:
			gen[cromosoma] = 0

	return gen

def elimina_peores_genes(poblacion, solucion):
	"""Elimina los dos peores genes"""
	adaptacion = evalua_poblacion(poblacion, solucion)
	i = adaptacion.index(min(adaptacion))
	del poblacion[i]
	del adaptacion[i]
	i = adaptacion.index(min(adaptacion))
	del poblacion[i]
	del adaptacion[i]

def mejor_gen(poblacion, solucion):
	"""Devuelve el mejor gen de la población"""
	adaptacion = evalua_poblacion(poblacion, solucion)

	return poblacion[ adaptacion.index(max(adaptacion)) ]

def algoritmo_genetico():
	# code here
	max_iter = 10
	max_poblacion = 50
	num_vars = 10
	fin = False
	solucion = poblacion_inicial(1, num_vars)[0]
	poblacion = poblacion_inicial(max_poblacion, num_vars)

	iteraciones = 0
	while not fin:
		iteraciones += 1
		for i in range(len(poblacion)//2):
			gen1, gen2 = seleccion(poblacion, solucion)
			nuevo_gen1, nuevo_gen2 = cruce(gen1, gen2)
			nuevo_gen1 = mutacion(0.1, nuevo_gen1)
			nuevo_gen2 = mutacion(0.1, nuevo_gen2)
			poblacion.append(nuevo_gen1)
			poblacion.append(nuevo_gen2)
			elimina_peores_genes(poblacion, solucion)
		
		if max_iter < iteraciones:
			fin = True

	print("Solución : " + str(solucion))
	mejor = mejor_gen(poblacion, solucion)

	return mejor, adaptacion_3sat(mejor, solucion)

if __name__ == '__main__':
	r.seed()
	mejor_gen = algoritmo_genetico()
	print("Mejor gen : " + str(mejor_gen[0]))
	print("Función de adaptación : " + str(mejor_gen[1]))
