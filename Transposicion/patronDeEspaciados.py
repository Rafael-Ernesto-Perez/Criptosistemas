#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:16:33 2019

@author: Rafael Ernesto Perez

"""
from __future__ import unicode_literals
import operator


import transposition_cripto_ataque_v1 as t
cadena = "ΣΦΨΞΔλΨΔΛΣΦΔλΨξΔϗΞΔΦΨΞϑλΨΛΣΘϑΞϗΦϑλΨΣΞΨλϑΞΨζβΣφΔΨΣΦΨΣΞΨξΛϗΞΞϑΨϖΣΞΨΠΣϖΛΣφΔΞΨΩΨΠΛΣΦϖϗϖϑΨΔΨΞΔΨΘΔφϗΔΨϖΣΨΞϑλΨΓΔΘϗΦϑλΨΣΞΨΔΛΛϗΣΛϑΨαΔΨΣΞΨΔΛΛϗΣΛϑΨαΔΨΣλΨξΔΦϖΣΛΔΨϖΣΨΦϗΣξΞΔΨλβΨΠϑΦΓΡϑΨΔΞΨαϗΣΦμϑΨΞϑΨλΔΞβϖΔΦΨΞΔλΨεΞΔβμΔλΨϖΣΞΨΠΔζϑΦΔΞΨΩΨΔΦϗΘΔΦϖϑΨΞΔΨμΛϑΠΔΨΠΔΛΨΣλϑλΨΓΣΛΛϑλΨΣΞΨΔΛΛϗΣΛϑΨαΔΨΣΞΨΔΛΛϗΣΛϑΨαΔΨΞΔλΨΠΣΦΔλΨΩΨΞΔλΨαΔηβϗμΔλΨλΣΨαΔΦΨΠΔΛΨΞΔΨΘϗλΘΔΨλΣΦϖΔΨΞΔλΨΠΣΦΔλΨλϑΦΨϖΣΨΦϑλϑμΛϑλΨΞΔλΨαΔηβϗμΔλΨλϑΦΨΔζΣΦΔλ"

#Sustitucion online español (SE APLICO SUSTITUCION MONOALFABETICA):
cadena="ENALOSAORENOSABOULONALISAREMILUNISAELASILAVYEGOAENAELABRULLIADELAPEDREGOLAHAPRENDUDIAOALOAMOGUOADEALISAJOMUNISAELAORRUERIACOAELAORRUERIACOAESABONDEROADEANUEBLOASYAPINJXIAOLACUENTIALIASOLYDONALOSAFLOYTOSADELAPOVINOLAHAONUMONDIALOATRIPOAPORAESISAJERRISAELAORRUERIACOAELAORRUERIACOALOSAPENOSAHALOSACOZYUTOSASEACONAPORALOAMUSMOASENDOALOSAPENOSASINADEANISITRISALOSACOZYUTOSASINAOVENOS"
#Sustitucion online ingles:
#cadena="ONTRESTELONESTBEIRENTRASTLOWARINASTORTSARTDUOVETONTORTBLIRRATGORTMOGLOVERTYTMLONGIGATETRETWEVIETGOTRASTFEWINASTORTELLIOLATHETORTELLIOLATHETOSTBENGOLETGOTNIOBRETSUTMANFKATERTHIONCATRATSERUGENTRESTPREUCESTGORTMEDANERTYTENIWENGATRETCLAMETMELTOSASTFOLLASTORTELLIOLATHETORTELLIOLATHETRESTMONESTYTRESTHEQUICESTSOTHENTMELTRETWISWETSONGETRESTMONESTSANTGOTNASACLASTRESTHEQUICESTSANTEDONES"

#Posible encryption :
#Clave 1: EN LOS ORENOS BOULON LIS REMILUNIS EL SIL VYEGO EN EL BRULLI DEL PEDREGOL H PRENDUDI O LO MOGUO DE L
#EN LOS ORENOS BOULON LIS REMILUNIS EL SIL VYEGO EN EL BRULLI DEL PEDREGOL H PRENDUDI O LO MOGUO DE LIS JOMUNIS EL ORRUERI CO EL ORRUERI CO ES BONDERO DE NUEBLO SY PINJXI OL CUENTI LI SOLYDON LOS FLOYTOS DEL POVINOL H ONUMONDI LO TRIPO POR ESIS JERRIS EL ORRUERI CO EL ORRUERI CO LOS PENOS H LOS COZYUTOS SE CON POR LO MUSMO SENDO LOS PENOS SIN DE NISITRIS LOS COZYUTOS SIN OVENOS
#a-" ";o-a;u-i;i-o ==> en las arenas bailan los remolinos el sol

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in abecedario:
    if c in cadena:
        new_cadena = cadena.replace(c, " ")
        print("cadena = \""+new_cadena+"\"")
        print(" ")
        print (t.ataqueTransposition(new_cadena))
    print(" ")