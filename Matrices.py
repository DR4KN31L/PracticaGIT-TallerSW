# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:09:21 2020

@author: s112e10
"""

'''
una funcion que reciba dos matrices de tamaño diferente n*m y n*x, 
llenarla con numeros aleatorios,los tamaños se le piden al usuario, 
se les hace el producto punto,cambiar por -1 o 0 los numeros primos
'''
import numpy as np
 
#funcion para crear matrices
def crearMatrices():
    print("Para la matriz nxm ")
    n=int(input("Ingrese el valor de n: "))
    m=int(input("Ingrese el valor de m: "))
    print("Para la matriz nxy ")
    y=int(input("Ingrese el valor de y: "))
    print("generando matriz...")
    nm=np.random.randint(0,100,size=(n,m))
    my=np.random.randint(0,100,size=(m,y))
    
    nm=np.reshape(nm,(n,m))
    my=np.reshape(my,(m,y))
    
    print(nm,'\n',my)
    print(np.dot(nm,my))
    
    return nm,my

#Funcion para obtener el producto punto
def productoPunto(matriz1,matriz2):
    return np.dot(matriz1,matriz2)


def reemplazarPrimosNorteños(matriz):

    
    
    
    
    
a,b=crearMatrices()
m=productoPunto(a,b)
print(m) 