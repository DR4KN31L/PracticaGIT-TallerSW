# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:09:21 2020

@author: s112e10
"""

'''
una funcion que reciba dos matrices de tamaño diferente n*m y n*x, 
llenarla con numeros aleatorios,los tamaños se le piden al usuario, 
se les hace el producto cruz,cambiar por -1 o 0 los numeros primos
'''
 import numpy as np
 
def crearMatrices():
    print("Para la matriz nxm ")
    n=input("Ingrese el valor de n: ")
    m=input("Ingrese el valor de m: ")
    print("generando matriz...")
    nm=np.random.randint(100,size=(n,m))
    print(nm)
    print("Para la matriz nxy ")
    y=input("Ingrese el valor de y: ")
    print("generando matriz...")
    nx=np.random.randint(100,size=(x,n))
    print(nx)
    