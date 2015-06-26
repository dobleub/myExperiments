#! /usr/bin/env python
# -*- coding: utf-8 -*-

def div():
	numero1 = int(raw_input("numero: "))
	numero2 = int(raw_input("numero: "))
	cociente = numero1 / numero2
	residuo = (cociente * numero2) - numero1
	
	print abs(residuo)

## MAIN
if __name__=="__main__":
	div()
	
	
	

