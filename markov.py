#!/usr/local/bin/python

#Importamos dos módulos

import random
#utilizado para escoger un elementos
#aleatorio de una lista

import sys
#permite acceder a algunas clases
#utilizadas por el intérprete

no_palabra = "\n" 
w1 = no_palabra
w2 = no_palabra

# GENERAMOS EL DICCIONARIO
dict = {}

for linea in sys.stdin:
    for palabra in linea.split():
        dict.setdefault( (w1, w2), [] ).append(palabra)
        w1 = w2
        w2 = palabra

# Fin de archivo
dict.setdefault((w1, w2), [] ).append(no_palabra)

# GENERAMOS LA SALIDA
w1 = no_palabra
w2 = no_palabra

# puedes modificarlo
max_palabras = 10000

for i in xrange(max_palabras):
    nueva_palabra = random.choice(dict[(w1, w2)])

    if nueva_palabra == no_palabra:
        sys.exit() 

    print nueva_palabra;

    w1 = w2
    w2 = nueva_palabra