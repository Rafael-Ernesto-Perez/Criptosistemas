#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import operator


class Main:
    def __init__(self):

        print "Bienvenido a Cript Griego"

        self.cadena = "ΨφΔξβΨμλΓΛ ΡΘξΡΛξΠμφ λΨξΘΓΠμΓΔ ΨξΛφζΡμλΓ ΔξΛφζΡμλΓ ΔξΛφζΡμλΓ ΔξΨφΔξΡΛξ μηφΔΨξΔΡξ μΨλΓΘξαΓΔ ΡΩΓΘξΣΡΔξ ΡΩξλμΨΩΨξ ΓξΛΓξΩΨζΛ ΡξφΠηΓΛΔΓ ΔξΦΓξΘηξλ μΨΩΨξΔφΠΩ φΘφβΨξΓζμ φΡμΨΩξΛΓΘ ξΞμΨΣφΩαφ ΓΘξηΩφΔΓΘ ξΔΡΛξΘηΔξ ΦξΛΨΘξΛφζ μΡΘξΔΡΛξβ ηΩΔΨξμΡΘΞ ΨΩΔΡΩξΓΛξ ΠμΓΩξΞηΡζ ΛΨξΓμΠΡΩλ φΩΨξΘΓΛηΔ ξΓΛξΠμΓΩξ ΞηΡζΛΨξΓμ ΠΡΩλφΩΨξΘ ΓΛηΔξΦξΛΨ ΘξΛφζμΡΘξ ΔΡΛξβηΩΔΨ ξμΡΘΞΨΩΔΡ ΩξΓΛξΠμΓΩ ξΞηΡζΛΨξΓ μΠΡΩλφΩΨξ ΘΓΛηΔξΦξΛ ΨΘξΛφζμΡΘ ξΔΡΛξβηΩΔ ΨξμΡΘΞΨΩΔ ΡΩξΓΛξΠμΓ ΩξΞηΡζΛΨξ ΓμΠΡΩλφΩΨ ξΘΓΛηΔξαΨ μΨξΘΡΓΩξΡ λΡμΩΨΘξΛΨ ΘξΛΓημΡΛΡ ΘξϑηΡξΘηΞ φβΨΘξαΨΩΘ ΡΠηφμξϑηΡ ξΘηΞφβΨΘξ αΨΩΘΡΠηφμ ξαΨμΨΩΓΔΨ ΘξΔΡξΠΛΨμ φΓξΣφΣΓβΨ ΘξΨξεημΡβ ΨΘξαΨΩξΠΛ ΨμφΓξβΨμφ μξΨξεημΡβ ΨΘξαΨΩξΠΛ ΨμφΓξβΨμφ μξΨξεημΡβ ΨΘξαΨΩξΠΛ ΨμφΓξβΨμφ μ"

        self.griegoNumerico = {"Ψ": 700, "φ": 500, "Δ": 4, "ξ": 60, "β": 2, "μ": 40, "λ": 30, "Γ": 3,
                               "Λ": 30, "Ρ": 100, "Θ": 9, "Π": 80, "ζ": 7, "η": 8, "α": 1, "Ω": 800,
                               "Σ": 200, "Φ": 500, "Ξ": 60, "ϑ": 9, "ε": 5}

        self.griegoAlfabetico = {'α': 'a', 'β': 'b', 'Γ': 'g', 'Δ': 'd', 'η': 'h', 'Θ': 'th', 'λ': 'l', 'μ': 'm',
                                 'Ξ': 'X', 'Ψ': 'ps', 'φ': 'ph', 'Λ': 'L', 'ξ': 'x', 'Π': 'P', 'Ρ': 'R', 'Ω': 'O',
                                 'ϑ': 'th', 'ε': 'E', 'Σ': 'S', 'ζ': 'Z', 'Φ': 'Ph', ' ': ' '}

        self.porcentajesIngles = {"a": 8.167, "b": 1.492, "c": 2.782, "d": 4.253, "e": 12.702, "f": 2.228, "g": 2.015,
                                  "h": 6.094,
                                  "i": 6.966, "j": 0.153, "k": 0.772, "l": 4.025, "m": 2.406, "n": 6.749, "o": 7.507,
                                  "p": 1.929,
                                  "q": 0.095, "r": 5.987, "s": 6.327, "t": 9.056, "u": 2.758, "v": 0.978, "w": 2.360,
                                  "x": 0.150,
                                  "y": 1.974, "z": 0.074}

        self.porcentajesAleman = {"a": 6.51, "b": 1.89, "c": 3.06, "d": 5.08, "e": 17.40, "f": 1.66, "g": 3.01,
                                  "h": 4.76, "i": 7.55, "j": 0.27, "k": 1.21, "l": 3.44, "m": 2.53, "n": 9.78,
                                  "o": 2.51, "p": 0.79, "q": 0.02, "r": 7.00, "s": 7.27, "t": 6.15, "u": 4.35,
                                  "v": 0.67, "w": 1.89, "x": 0.03, "y": 0.04, "z": 1.13}

        self.porcentajesEspanol = {"a": 12.53, "b": 1.42, "c": 4.68, "d": 5.86, "e": 13.68, "f": 0.69, "g": 1.01,
                                   "h": 0.70, "i": 6.25, "j": 0.44, "k": 0.00, "l": 4.97, "m": 3.15, "n": 6.71,
                                   "o": 8.68, "p": 2.51, "q": 0.88, "r": 6.87, "s": 7.98, "t": 4.63, "u": 3.93,
                                   "v": 0.90, "w": 0.02, "x": 0.22, "y": 0.90, "z": 0.52}

        self.porcentajesFrances = {"a": 7.636, "b": 0.901, "c": 3.260, "d": 3.669, "e": 14.715, "f": 1.066, "g": 0.866,
                                   "h": 0.737, "i": 7.529, "j": 0.545, "k": 0.049, "l": 5.456, "m": 2.968, "n": 7.095,
                                   "o": 5.378, "p": 3.021, "q": 1.362, "r": 6.553, "s": 7.948, "t": 7.244, "u": 6.311,
                                   "v": 1.628, "w": 0.114, "x": 0.387, "y": 0.308, "z": 0.136}

        self.porcentajesCadena = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1,
                                  "h": 1, "i": 1, "j": 1, "k": 1, "l": 1, "m": 1, "n": 1,
                                  "o": 1, "p": 1, "q": 1, "r": 1, "s": 1, "t": 1, "u": 1,
                                  "v": 1, "w": 1, "x": 1, "y": 1, "z": 1}

        self.totalCaracteres = 0
        self.inicio()
        self.porcentajes()

    def inicio(self):
        print "Bloque   ValorNumerico"
        self.decifrar(self.cadena, self.griegoNumerico)
        print "Bloque   ValorAlfabetico"
        self.decifrar(self.cadena, self.griegoAlfabetico)
        self.frecuencias(self.cadena, self.griegoNumerico)
        self.frecuencias(self.cadena, self.griegoAlfabetico)

    def decifrar(self, cadena, diccionario):
        bloque = []
        elementos = ''
        for i in cadena:
            if i == ' ':
                bloque.append(elementos)
                elementos = ''
            else:
                if diccionario.get(i):
                    elementos += str(diccionario[i])
                else:
                    print "no existe", i
        item = 0
        for i in bloque:
            item += 1
            print item, ": \t", i
        print ""

    def frecuencias(self, cadena, diccionario):
        bloque = []
        elementos = ''
        # reseteo par contar
        auxiliar = {}
        self.totalCaracteres = 0  # borro cargas de otros llamados
        print ""
        print " \t frecuencias \t"
        print "item \t  griego \t  equivalenciaEspañol \t frecuencia \t"
        for i in diccionario:
            auxiliar[i] = 1

        for i in cadena:
            if i == ' ':
                bloque.append(elementos)
                elementos = ''
            else:
                if auxiliar.get(i):
                    auxiliar[i] += 1
                    self.totalCaracteres += 1
                else:
                    print "no existe", i
        item = 0
        ordenados = sorted(auxiliar.items(), key=operator.itemgetter(1))
        ordenados.reverse()
        print ""
        print "self.totalCaracteres ", self.totalCaracteres

        for i in ordenados:
            item += 1
            a = diccionario[i[0]]
            valorCorregido = i[1] - 1
            if valorCorregido > 0:
                porcentaje = (valorCorregido * 100) / self.totalCaracteres
            else:
                porcentaje = 0

            print item, ": \t", i[0], " \t", a, " \t", " \t", " \t", valorCorregido, " \t", porcentaje

            # grabo frecuencias del la cadena
            print "-------------",self.porcentajesCadena['a']
            if self.porcentajesCadena.get(a):
                self.porcentajesCadena[a] = porcentaje

                ############################Overfitting##################
        print ""

    def porcentajes(self):
        valorCaracter = [0, 0, 0, 0]  # INGLES, FRANCES, ALEMAN, ESPANOL
        valorTotal = [0, 0, 0, 0]  # INGLES, FRANCES, ALEMAN, ESPANOL

        for i in self.porcentajesCadena:
            if self.porcentajesIngles.get(i):
                valorCaracter[0] = self.porcentajesIngles[i]
            if self.porcentajesFrances.get(i):
                valorCaracter[1] = self.porcentajesFrances[i]
            if self.porcentajesAleman.get(i):
                valorCaracter[2] = self.porcentajesAleman[i]
            if self.porcentajesEspanol.get(i):
                valorCaracter[3] = self.porcentajesEspanol[i]
            menorDiferencia = 9999
            menorIndex = 0
            
            for j in valorCaracter:
                #print "letra porc ",i, self.porcentajesCadena[i]
		#print "j: ", j
                diferencia=abs(self.porcentajesCadena[i] - j)
                if  diferencia < menorDiferencia:
                      menorDiferencia = diferencia
                      menorIndex=valorCaracter.index(j)
            valorTotal[menorIndex] +=1
            #print "max:",valorCaracter, max(valorCaracter), valorCaracter.index(max(valorCaracter))
	

	acertados=max(valorTotal)
	itemIdioma=valorTotal.index(acertados)            
        print "Total: ", valorTotal
	if itemIdioma == 0:
		print "Ingles"
        if itemIdioma == 1:
                print "Frances"
        if itemIdioma == 2:
                print "Aleman"
        if itemIdioma == 3:
                print "Espanol"

if __name__ == '__main__':
    main = Main()
