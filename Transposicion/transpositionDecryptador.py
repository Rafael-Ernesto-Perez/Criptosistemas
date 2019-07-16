#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 5 23:58:33 2019

@author: Rafael Ernesto Perez

"""

import math, pyperclip

def main():
    cadena = 'Cenoonommstmme oo snnio. s s c'
    clave = 8

    texto_plano = decryptMensaje(clave, cadena)
    #hay los espacios al final del mensaje descifrado
    print(texto_plano + '|')

    pyperclip.copy(texto_plano)


def decryptMensaje(clave, mensaje):
    #algoritmo de transposicion basico
    numero_de_columnas = math.ceil(len(mensaje) / clave)
    numero_de_filas = clave
    numero_de_grupos = (numero_de_columnas * numero_de_filas) - len(mensaje)
    texto_plano = [''] * numero_de_columnas

    col = 0
    fil = 0
    for symbolo in mensaje:
        texto_plano[col] += symbolo
        col += 1 # muevo a la proxima columna
        if (col == numero_de_columnas) or (col == numero_de_columnas - 1 and fil >= numero_de_filas - numero_de_grupos):
            col = 0
            fil += 1

    return ''.join(texto_plano)


if __name__ == '__main__':
    main()