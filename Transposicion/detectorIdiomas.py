#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 6 05:10:20 2019

@author: Rafael Ernesto Perez

"""
letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_y_espacios = letras_mayusculas + letras_mayusculas.lower() + ' \t\n'

def leerDiccionario():
    #diccionario = open('../diccionarios/words_español.txt')
    diccionario = open('../diccionarios/words_español.txt')#cambiar cuando se requiera
    palabras_x = {}
    for palabras in diccionario.read().split('\n'):
        palabras_x[palabras.upper()] = None
    diccionario.close()
    return palabras_x

palabras_del_idioma_x = leerDiccionario()


def contadorIdiomaX(cadena):
    cadena = cadena.upper()
    cadena = elimaLetrasInvalidas(cadena)
    posibles_palabras = cadena.split()

    if posibles_palabras == []:
        return 0.0 # no palabrass at all, so return 0.0

    encontrados = 0
    for palabras in posibles_palabras:
        if palabras in palabras_del_idioma_x:
            encontrados += 1
    return float(encontrados) / len(posibles_palabras)


def elimaLetrasInvalidas(cadena):
    lettersOnly = []
    for symbol in cadena:
        if symbol in letras_y_espacios:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def esIdiomaX(cadena, palabrasPercentage=20, letterPercentage=85):
    # Por Defecto, 20 % de los palabras debe existir en el archivo del diccionario, y
    # 85 el % de todos los personajes en cadena deben ser letras o espacios
    # (no contepla el acentos o números).
    palabrasEncontradras = contadorIdiomaX(cadena) * 100 >= palabrasPercentage
    numero_de_letras = len(elimaLetrasInvalidas(cadena))
    porcentajes_letras = float(numero_de_letras) / len(cadena) * 100
    letras_encontradas = porcentajes_letras >= letterPercentage
    return palabrasEncontradras and letras_encontradas


print (esIdiomaX("hola probando si soy español"))