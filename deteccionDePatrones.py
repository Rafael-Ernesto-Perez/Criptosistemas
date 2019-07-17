#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Jun 28 21:10:32 2019

@author: Rafael Perez

"""

from __future__ import unicode_literals

#Librerias
import numpy as np
import operator


cadena  ="asdholafgchauhjholaklchaujklhola"
print(len(cadena))
tamanio=len(cadena)+1
bloque = []
frecuenciaPalab = []
diccionario = {}
ci=0

for i in range(0,tamanio):
	ci+=1
	for j in range(i,tamanio):
		if (cadena[i:j]) != '' and len(cadena[i:j])>1:
			bloque.append(cadena[i:j])

#bloque.remove('')
def Acortar(w,izquierda,derecha):
	try: #elimina subconjunto de la palabra mayor (mayor en algun momento)
		for i in range(izquierda,len(w)+derecha):#truco para no eliminar palabra de mayor longitud
			for j in range(i,len(w)+derecha):
				key=w[i:j]
				if key != '' and len(key) > 1:
					#print(key)					
					if diccionario.get(key):
						diccionario.pop(key)
						#print ("eliminado: ",key)               	
	except ValueError:
		return



def Posiciones(w):
	lista = []
	pos_inicial = -1
	try:
		while True:
			# cada vez buscamos desde un caracter más adelante de
			# la última ocurrencia encontrada
			pos_inicial = cadena.index(w, pos_inicial+1)
			lista.append(pos_inicial)
	except ValueError: # cuando ya no se encuentre la letra
		#print ('Posiciones de la letra "e" en la cadena:', lista)
		return lista

ci=0
posiciones_i = []
for w in bloque:
	#print("grupo:",ci)
	ci+=1	
	if bloque.count(w) > 1:
		longitud=len(w)
		apariciones=bloque.count(w)
		Acortar(w,0,0)
		posiciones_i = Posiciones(w)
		diccionario[w] = [longitud,apariciones,posiciones_i]
		frecuenciaPalab.append([longitud,apariciones,w])
#print('frecuenciaPalab', frecuenciaPalab) 

for palabra, frecuencias in sorted(diccionario.items(), key=operator.itemgetter(1)):
   print (palabra, ":", frecuencias)
   Acortar(palabra,1,1)


print(" -------------------final recortado -------------")
f = open('patrones.txt','a')


for palabra, frecuencias in sorted(diccionario.items(), key=operator.itemgetter(1)):
   print (palabra, ":", frecuencias)
   #f.write('\n' + palabra+" frec:"+str(frecuencias)) # valido para alfanumericos corregir para que guarde simbolos especiales
f.close()
print(" ")
#ordenacion 2
#a=np.array(frecuenciaPalab)
#idx = np.lexsort((a[:,0]))
#frecuenciaPalab[idx]
#print('frecuenciaPalab', frecuenciaPalab) 


