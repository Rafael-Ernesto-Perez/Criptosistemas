#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 5 22:16:33 2019

@author: Rafael Ernesto Perez

"""

import pyperclip, transpositionDecryptador
from math import log10
import detectorIdiomas as dect

def main():
    #ejemplo 1
    mensaje = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

    mensajeAtacado = ataqueTransposition(mensaje)

    if mensajeAtacado == None:
        print('Fallo de ataque criptoanlitico.')
    else:
        print('Se copio al portapapeles el texto decifrado con exito:')
        print(mensajeAtacado)
        pyperclip.copy(mensajeAtacado)


def ataqueTransposition(mensaje):
    print('Atancado con tecnica: transposicion usando diccionario de estadisticas por idioma')
    print('(Presione Ctrl-C or Ctrl-D to quit at any time.)')

    # primero fuerza bruta a todas la posibles claves
    for clave in range(1, len(mensaje)):
        print('Trying clave #%s...' % (clave))

        texto_decifrado = transpositionDecryptador.decryptMensaje(clave, mensaje)

        if dect.esIdiomaX(texto_decifrado):
            print()
            print('Posible encryption :')
            print('Clave %s: %s' % (clave, texto_decifrado[:100]))
            print()
            print('Ingrese D para terminar, o presione Enter para continuar atacando:') # para seguir probandos otros casos
            repuesta = input('> ')

            if repuesta.strip().upper().startswith('D'):
                return texto_decifrado

    return None

if __name__ == '__main__':
    main()
