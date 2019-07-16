#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Fri 12 20:18:40 2019

@author: Rafael Ernesto Perez

"""
import pyperclip

#simbolos del alfabeto
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

    cadena = "¡Salve insigne y altiva Corrientes, Legendaria de invicto broquel, Colosal y gentil amazona Que en tu frente se ostenta un laurel! ¡Empujabas a tus hijos valientes A salvar a la Patria o morir, Y a tu sien arrogante la gloria Del laurel iba siempre a ceñir! Pago Largo, El Rincón y Corrientes Don Gonzalo, Ñaembé y Caá Guazú Son estrellas que fulgen de gloria En un cielo de hermoso tisú. De una aurora que se abre en la entrada Pedrería de un áureo joyel La simiente que en grato futuro Su guirnalda brotó de laurel. Ah, que tiempos aquellos! Tu nombre Al lanzar nuestra Patria en clamor, Resonaba en los pueblos del Plata Como un parche de ronco tambor. ¡Salve sacra heroína argentina, Templo augusto de patrio fervor, Alto faro de Áurea leyenda, Derramando prístino fulgor! Gloria excelsas a los manes ilustres De Alvear, San Martín y Cabral, De Berón, Madariaga y cien otros Que el chispear de su acero inmortal Desgarraron con nimbos de gloria De la Patria el sombrío capuz, Y en su historia fulguran gloriosos Como astros de espléndida luz Y a tus lanzas de gloria empolvadas No relucen como antes al sol Y el taller y la escuela te ufanan Que impulsar el progreso es turol Adelante soberbia patria Clamorosa con brío a vencer En las justas del arte y la ciencia De la industria, el comercio y taller" # himno de corrientes primer parrafo
    clave = 'claveab'
    modo = 'encrypt' # me permite usar menos parametros

    if modo == 'encrypt':
        traduccion = encryptMensaje(clave, cadena)
    elif modo == 'decrypt':
        traduccion = decryptMensaje(clave, cadena)

    print('%sed message:' % (modo.title()))
    print(traduccion)
    print (" ")
    print (decryptMensaje(clave, traduccion))
    pyperclip.copy(traduccion)
    print()
    print('The message has been copied to the clipboard.')


def encryptMensaje(clave, message):
    return translateMensaje(clave, message, 'encrypt')


def decryptMensaje(clave, message):
    return translateMensaje(clave, message, 'decrypt')


def translateMensaje(clave, message, mode):
    traduccion = [] # contiene cadena encriptada o desencriptada
    claveIndex = 0
    clave = clave.upper()

    for simbolo in message: 
        num = letras.find(simbolo.upper())
        if num != -1: # pasao todo a maysusculas para ser mas practico
            if mode == 'encrypt':
                num += letras.find(clave[claveIndex]) 
            elif mode == 'decrypt':
                num -= letras.find(clave[claveIndex]) 

            num %= len(letras) # deriva de la formula que genera la tabla 

            # dada la tablaa
            if simbolo.isupper():#defino movimiento en colunas
                traduccion.append(letras[num])
            elif simbolo.islower():
                traduccion.append(letras[num].lower())

            claveIndex += 1 
            if claveIndex == len(clave):
                claveIndex = 0
        else:
            # por si no aparece el simbolo
            traduccion.append(simbolo)

    #print (''.join(traduccion))
    return ''.join(traduccion)



if __name__ == '__main__':
    main()