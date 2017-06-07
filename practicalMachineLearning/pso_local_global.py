#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pso_local_global.py
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

# Algoritmo GBest
# Datos: C cúmulos de partículas, t iteraciones
# Resultado: conjunto de soluciones óptimas
# begin
# t <- 0 ;
# Genera cúmulo de partículas inicial ;
# for cada partícula i do
# 	Inicializar xi y vi aleatoriamente ;
# 	Evaluar xi en la función de aptitud ;
# 	Inicializar yi <- xi ;
# Seleccionar ýi ;
# while no se cumpla el criterio de terminación do
# 	for cada partícula i do
# 		for cada dimensión j do
# 			Calcular la velocidad de vij usando:
# 			vij(t+1) <- wvij(t) + c1r1(t)(yij(t)-xij(t)) + c2r2(t)(ýij(t)-xij(t)) ;
# 			Actualizar la posición de xij usando:
# 			xij(t+1) <- xij(t) + vij(t+1) ;
# 		Evaluar la nueva posición de xi ;
# 		if xi <= yi then
# 			yi <- xi ;
# 		if xi <= ýi then
# 			ýi <- xi ;
# 	t <- t+1;
# end
# 
# xi = (xi1, xi2, ..., xij) para i=[1:s], j=[1:n] : s = número de partículas y n = número de dimensiones
# w = factor de inercia
# w = [(wmin - wmax)/(itermax01)-(iter-1)]+wmax
# c1, c2 = coeficientes de aceleración
# r1, r2 = vectores aleatorios r1 = (r11, r12, ..., r1j), r2 = (r21, r22, ..., r2j) .: U[0:1]
# yi(t) = vector yi(t) = (yi1, yi2, ..., yij)(t), la mejor posición de la partícula lider
# ýi(t) = ýi(t) = (ýi1, ýi2, ..., ýij)(t), la mejor posición obtenida por los vecinos de la partícula xi en t
#  

def main():
	# code here

if __name__ == '__main__':
	main()
