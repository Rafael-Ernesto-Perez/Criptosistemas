#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Thu 11 02:20:04 2019

@author: Rafael Ernesto Perez

"""
import sys


def mcd( numeros ):
	# el script calcula el maximo comun divisor
	mcd = 1
	numeros.sort() #ordena la lista de menor a mayor
	for i in range( 2, numeros[-1]+1 ): #recorre hasta el numero mayor de la lista (el ultimo)
		if esDivisible(i, numeros):
			mcd = i
	return mcd

def esDivisible( numero, lista):
	divisible = True
	for i in lista:
		if not i % numero == 0:
			divisible = False
			break;
	return divisible #devuelve boolean

def validar( numeros ):
	correcto = True
	for i in numeros:
		try:
			valor = int(i)
			if valor <= 0:
				correcto = False
				break;
		except ValueError:	
			correcto = False
			break;
	return correcto

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		print (sys.argv[1:])
		if validar(sys.argv[1:]):
			lista = [ int(i) for i in sys.argv[1:] ]
			resultado = mcd ( lista )
			print ("MCD = ", resultado)
		else:
			print ("Solo se permite números enteros")
	
