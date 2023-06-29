# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 08:49:34 2023

@author: Admin
"""

import operator 

x=input("Enter a word: ")
y=set(x)
z=list(y)
Characters=dict.fromkeys(x,0)
w={}

for z in x:
    if z not in w:
        w[z]=1
        
    else:
        w[z]+=1
    w_lower = {k.lower(): v for k, v in w.items()}
    w_sorted = dict(sorted(w.items(), key = operator.itemgetter(1),reverse = True))  
        

print("The letters in order of frequency: ", w_sorted)    
    