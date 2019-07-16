#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 5 22:16:33 2019

@author: Rafael Ernesto Perez

"""
from __future__ import unicode_literals
import operator



cadena = "ζηΓΘμϠξαφ αηΓφλΠϠλζ αϑηΡΓζηΓΩ ηϖΓαΠξΔΡα λΡΓΩΡλβΔΔ ΡΓηΓζηΓϑΔ ϨΔΠϠηΓφλΣ μΠΓΩΡλΣλβ \
ΔΡΓΔζΓΞαΔ ΠΔϠξηΡΓΦΔ ΠΔΡηζΓΛΓη ϠΔΦμΡηΡΓζ λϠΓΞΔΠΔϨα φαλϠΓϑΔΓζ ηΓζαΞΔΡξη ϑΓΩηΡηΓΠλ ϠλξΡλϠΓΩη \
ΡηΓΠμΔϠξΡ ηΓΩλϠξΔΡα ϑηϑΓΛΓΩηΡ ηΓξλϑλϠΓζ λϠΓελΣΞΡΔ ϠΓϑΔζΓΣμΠ ϑλΓϗμΔΓϗμ αΔΡηΠΓεηΞ αξηΡΓΔΠΓΔ \
ζΓϠμΔζλΓη ΡΦΔΠξαΠλΓ αΠβλφηΠϑλ ΓζηΓΩΡλξΔ φφαλΠΓϑΔΓ ϑαλϠΓϨμΔΠ ξΔΓϑΔΓξλϑ ηΓΡηϖλΠΓΛ ΓΘμϠξαφαη \
ΓλΡϑΔΠηΣλ ϠΓϑΔφΡΔξη ΣλϠΓΛΓΔϠξ ηΞζΔφΔΣλϠ ΓΔϠξηΓφλΠ ϠξαξμφαλΠ ΓΩηΡηΓζηΓ ΠηφαλΠΓηΡ ΦΔΠξαΠη"
print(cadena.replace(' ', ''))# quito espacios
#cadena.replace("ϗ", "_")# quito espacios
#print(len(set(cadena))) #conjunto de símbolos 



abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = ''
letras = {}
idx = 0
for c in cadena:
    #print (c)
    #if c=="ϗ":
        #print (c," hay",abecedario[idx])
    if c not in letras:
        letras[c] = abecedario[idx]
        idx += 1
    t += letras[c]
#t=t.replace('I', '')# quito espacios
print(t)
print(" ")
f4g ={}    
f = open('../diccionarios/brut4g_es.txt')
total = 0  
for line in f:
    (w, c) = line.split(sep= ' ')
    f4g[w] = int(c)
    total += int(c)
for w in f4g:
    f4g[w] /= total  # obtengo las frecuencias
f.close
#print ("aqui ",f4g['vbuei'])

def score(s):
    produit = 1
    for i in range(len(s)-3):
        if s[i:i+4] in f4g:
            produit *= f4g[s[i:i+4]]
        else:
            produit *= 1e-100     
    return produit
#print (score('casa'))

from math import log10
def logscore(s):
    logsum = 0
    min_freq = 1e-100          
    #print("soy s : ",s)
    for i in range(len(s)-3):
        logsum += log10(f4g.get(s[i:i+4], min_freq))
    print(-logsum)
    return -logsum   
#print (logscore('Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. Considered a father of the computer, Babbage is credited with inventing the first mechanical computer that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbages original plans. Built to tolerances achievable in the 19th century, the success of the finished engine indicated that Babbages machine would have worked. Nine years later, the Science Museum completed the printer Babbage had designed for the difference engine.'))


def simple_substitution(alpha, s):
    r = ''
    for c in s:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  #alfabeto simple  
            r += alpha[ord(c)-ord('A')]  # 
        else:
            r += c   # on no cambia los caracteres no alfabéticos
    return r

#alphabet_cifrador  =  'HCIFSGTJOKRNEVDWLXAYMZPUBQ'#especie de clave de orden que contiene letras del alfabeto simple
#texto_plano='CASA DE MI TIA'
#print (simple_substitution ( alphabet_cifrador,texto_plano  ))
 
def inverse_alpha(alpha):
    perm = {}
    for i in range(26):
        perm[ord(alpha[i])-ord('A')] = chr(i+ord('A'));
    return ''.join([perm[i] for i in range(26)])

#alphabet_decifrado = inverse_alpha(alphabet_cifrador)
#texto_cifrado=simple_substitution ( alphabet_cifrador,texto_plano )
#print (simple_substitution(alphabet_decifrado, texto_cifrado))


def string_shuffle( s ):
    c = list(s)
    random.shuffle(c)
    return ''.join(c)

import random
def aleatorio(alpha):
    c = list(alpha)
    i = random.randint(0,25)
    j = random.randint(0,25)
    while j == i:
        j = random.randint(0,25)  
    if random.random() < 0.5:
        c[i], c[j] = c[j], c[i] # permutacion
    else:
        if i > j:
            i, j = j, i            
        m = c[i:j]
        m.append(m.pop(0))      # rotacion
        c[i:j] = m
    return ''.join(c)

          
from math import exp
def criterioMetropolis(delta, T):
    if delta <= 0: return True
    if random.random() < exp(-delta/T): return True
    return False


def simulacionSubstitucionMonoalfabetica(crypto, max_iter = 8000, CoolRatio = 0.8 ):
    alpha = string_shuffle('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    old_score = logscore(simple_substitution(alpha, crypto))
    T = 0
    for i in range(100):  # 100 tirages pour avoir un ordre de grandeur de delta
        alpha = string_shuffle(alpha)
        new_score = logscore(simple_substitution(alpha, crypto))
        delta = new_score - old_score
        if delta > T: T = delta
        old_score = new_score
    T *= 10               
    best_alpha = alpha
    best_score = old_score
    freeze = 0
    while True:
        nb_iter = 0
        while nb_iter < max_iter:
            nalpha = aleatorio(alpha)
            new_score = logscore(simple_substitution(nalpha, crypto))
            delta = new_score - old_score
            if criterioMetropolis(delta, T): 
                alpha = nalpha
                old_score = new_score
                if old_score < best_score:
                    best_score = old_score
                    best_alpha = alpha
                    print(best_score)     
                    print(simple_substitution(best_alpha, crypto))
                    print('------')
                freeze = 0
            else:                            
                freeze += 1
            nb_iter += 1
        T *= CoolRatio
        if freeze > 25:    
            break
    print("*** Mejor Solucion ***")
    print('puntaje = ', best_score)
    print('alfabeto de decifrado :', best_alpha)
    print(simple_substitution(best_alpha, crypto))


#crypto1 = 'INELASEARINASEGAOLANELUSERIHULONUSEILESULEZDIVAEINEILEGROLLUEPILECIPRIVALEXECRINPOPUEAELAEHAVOAEPIELUSETAHONUSEILEARROIRUEMAEILEARROIRUEMAEISEGANPIRAEPIENOIGLAESDECUNTQUEALEMOINFUELUESALDPANELASEBLADFASEPILECAZUNALEXEANOHANPUELAEFRUCAECAREISUSETIRRUSEILEARROIRUEMAEILEARROIRUEMAELASECINASEXELASEMAYDOFASESIEMANECARELAEHOSHAESINPAELASECINASESUNEPIENUSUFRUSELASEMAYDOFASESUNEAZINAS'

simulacionSubstitucionMonoalfabetica(t,1000)