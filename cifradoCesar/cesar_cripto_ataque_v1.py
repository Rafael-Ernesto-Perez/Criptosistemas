#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:50:14 2019

@author: Rafael Ernesto Perez

"""
from __future__ import unicode_literals
import operator
from math import log10

#print(cadena.replace(' ', ''))# quito espacios
#print(len(set(cadena))) #conjunto de símbolos 
f4g ={}    # dic des fréquences des 4-grammes
f = open('../diccionarios/brut4g_es.txt')
total = 0  # effectif total
for line in f:
    (w, c) = line.split(sep= ' ')
    f4g[w] = int(c)
    total += int(c)
for w in f4g:
    f4g[w] /= total  # calcul des fréquences
f.close


def Cesar ( cadena, n):
    r = ''    # résultat
    for c in cadena:
        r += chr((ord(c)-ord('A')+ n)%26 +ord('A'))
    return r

#Cesar('CARPEDIEM', 7)
from math import log10
def logscore(s):
    logsum = 0
    min_freq = 1e-100          # fréquence d'un 4gramme inexistant
    for i in range(len(s)-3):
        logsum += log10(f4g.get(s[i:i+4], min_freq))
    return -logsum

def decrypter_Cesar( crypto ):
    clair = ''                     # mensaje de texto en claro
    meilleur_score = float('inf')  # + infinito
    for n in range(1, 26):
        test = Cesar(crypto, n)
        score = logscore(test)
        if (score < meilleur_score):
            meilleur_score = score
            clair = test
    return clair

cadena = "VDÑXGRV GHVGH FRUULHPWHV FDSLWDÑ, DUJHPWLPD"
print ("Texto cifrado : ", cadena)
print ("Texto decifrado: ",decrypter_Cesar(cadena))  

