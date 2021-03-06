#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  Generated by Geany 1.22
#  
#  Author:	Edward Osorio S.
#  Date:	2014-12-13
#  Version:	1.0
#  Mail:	osorio.edd@gmail.com
#  
#  Copyright 2014
#  

import os
import xlwt
import re

def changeData(array):
	tmpArray = []
	for element in array:
		tmp = element
		if tmp.find('\xc3\xa1') != -1:
			tmp = tmp.replace('\xc3\xa1','\xe1')
		if tmp.find('\xc3\xa9') != -1:
			tmp = tmp.replace('\xc3\xa9','\xe9')
		if tmp.find('\xc3\xad') != -1:
			tmp = tmp.replace('\xc3\xad','\xed')
		if tmp.find('\xc3\xb3') != -1:
			tmp = tmp.replace('\xc3\xb3','\xf3')
		if tmp.find('\xc3\xba') != -1:
			tmp = tmp.replace('\xc3\xba','\xfa')
		if tmp.find('\xc3\x81') != -1:
			tmp = tmp.replace('\xc3\x81','\xc1')
		if tmp.find('\xc3\x89') != -1:
			tmp = tmp.replace('\xc3\x89','\xc9')
		if tmp.find('\xc3\x8d') != -1:
			tmp = tmp.replace('\xc3\x8d','\xcd')
		if tmp.find('\xc3\x93') != -1:
			tmp = tmp.replace('\xc3\x93','\xd3')
		if tmp.find('\xc3\x9a') != -1:
			tmp = tmp.replace('\xc3\x9a','\xda')
		if tmp.find('\xc3\xb1') != -1:
			tmp = tmp.replace('\xc3\xb1','\xf1')
		if tmp.find('\xc3\x91') != -1:
			tmp = tmp.replace('\xc3\x91','\xd1')
		tmpArray.append(tmp)
		
	return tmpArray

def main():
	path = os.path.dirname(os.path.abspath(__file__))
	tmpFileName = os.path.abspath(__file__).split('/')	#linux
	#tmpFileName = os.path.abspath(__file__).split('\\')	#windows
	
	#path = '/home/dobleub/Github/posgradostnm/basicapp/docs/oficios/posgrados/'	# linux
	#path = 'C:\Ruta\a\directorio' #windows verificar que la ruta de directorio no termine en contra-diagonal
	
	style0 = xlwt.easyxf('font:bold on')
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Lista', cell_overwrite_ok=True);
	
	lstNames = []
	lstFirstNames = []
	lstDir = os.walk(path)
	
	for root, dirs, files in lstDir:
		for fichero in files:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if(extension == ".pdf" or extension == ".PDF"):
				if re.search(r'[+]',nombreFichero):						# verifica que el nombre de archivo para el encabezado
					tmpName = re.sub(r'[+]',"",nombreFichero)			# de la lista contenga un signo de +
					tmplst = tmpName.split(' ')
					lstFirstNames = changeData(tmplst)
				else:
					tmplst = nombreFichero.split(' ')
					lst = []
					for i in tmplst:
						if i.count('.') >= 1:
							i = i.replace('.',' ')
							if tmplst[0] == 'DOC':
								i = 'Doctorado en Ciencias ' + i
							if tmplst[0] == 'MOI':
								i = 'Maestría en Ciencias ' + i
							if tmplst[0] == 'MOP':
								i = 'Maestría ' + i
							if tmplst[0] == 'ESP':
								i = 'Especialización ' + i
						lst.append(i)
					lstNames.append(changeData(lst))
	
	for i,e in enumerate(lstFirstNames):
		ws.write(0,i,e.decode('iso-8859-1'),style0)
	
	for i,row in enumerate(lstNames):
		for j,col in enumerate(row):
			ws.write(i+1,j,col.decode('iso-8859-1'))
	
	fileName = tmpFileName[-1].split('.')
	wb.save(path + '/'+fileName[0]+'.xls')		#linux
	#wb.save(path + '\\'+fileName[0]+'.xls')		#windows
	
	return 0

if __name__ == '__main__':
	main()
