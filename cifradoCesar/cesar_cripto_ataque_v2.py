#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:50:14 2019

@author: Rafael Ernesto Perez

"""

from __future__ import unicode_literals
import operator
from math import log10

content = "OV M1SZ3YKXKVS2S2 O2 VK ZK13O NO VK M1SZ3YVYQSK 04O 2O NONSMK KV O234NSY NO 2S23OWK2 M1SZ3YQ1KPSMY2 MYX OV PSX NO OXMYX31K1 NOLSVSNKNO2 OX VY2 2S23OWK2 8 1YWZO1 24 2OQ41SNKN 2SX OV MYXYMSWSOX3Y NO SXPY1WKMSYX 2OM1O3K  OX OV VOXQ4KTO XY 3OMXSMY  2O MYXYMO O23K Z1KM3SMK MYWY 1YWZO1 Y PY19K1 OV MYNSQY  K4X04O O23K O7Z1O2SYX 3SOXO 4X 2SQXSPSMKNY O2ZOMSPSMY NOX31Y NOV K1QY3 3OMXSMY  K VK2 ZO12YXK2 04O 2O NONSMKX KV M1SZ3YKXKVS2S2 2O VO2 VVKWK M1SZ3YKXKVS23K2"
def count(content):
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        print(c, " appears ", content.count(c))

count(content)

def encrypt(content, n):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([alphabets[(alphabets.index(c) + n + len(alphabets)) % len(alphabets)] if c in alphabets else c for c in content])
print (encrypt(content, -9))