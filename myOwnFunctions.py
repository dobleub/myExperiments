#! /usr/bin/env python
# -*- coding: utf-8 -*-

def distancia(x1,y1,x2,y2):
	d = sqrt(((x2-x1)**2) + ((y2-y1)**2))
	return "d: " + '%6.3f' % (d)
#
def factorial(n): 
	try:
		num = int(n)
		if num < 0:
			print "Numero invalido"
		else:
			if num == 0:
				return num
			else:
				return  (num * factorial(num-1))
	except:
		print "Numero invalido"
#
def fibonacci(n):
	try:
		num = int(n)
		if num < 0:
			print "Numero invalido"
		else:
			if n == 0 or n == 1:
				return 1
			else:
				return fibonacci(n-1) + fibonacci(n-2)
	except:
		print "Numero invalido"
#
def multiplo(n):
	try:
		num = int(n)
		i=1
		while i <= 6:
			print n * i, '\t',
			i = i + 1
		print
	except:
		print "Numero invalido"
#
def binario1(n):
	"""este primer algoritmo utiliza la formula n = 2k + b"""
	if n == 0 or n == 1: return str(n)
	k = n / 2
	E = binario1(k)
	b = n % 2
	
	return str(E) + str(b)
#
def binario2(n):
	"""y este va recorriendo 1 bit hacia la derecha en cada iteracion"""
	if n == 0: return str(n)
	b = ''
	while n > 0:
		b = str(n % 2) + b
		n >>= 1
		#de esta forma el numero se va dividiendo entre 2 para llegar a 0 y terminar el bucle
		#tambien podria ser de esta forma: n /= 2 
    return b
#
def get_size(the_path):
    """Get size of a directory tree or a file in bytes."""
    path_size = 0
    for path, directories, files in os.walk(the_path):
        for filename in files:
            path_size += os.lstat(os.path.join(path, filename)).st_size
        for directory in directories:
            path_size += os.lstat(os.path.join(path, directory)).st_size
    path_size += os.path.getsize(the_path)
    return path_size
#
def verificar_primo(numero):
	rango = range(2,numero)
	if numero == 1:
		return "No es primo"
	elif numero == 2:
		return "Es primo"
	else:
		for elementos in rango:
			if numero % elementos == 0:
				print "No es primo"
				break
			else:
				if elementos == numero - 1:
					print "Es primo"
