#!/usr/bin/env python
#Lab_01
#Primero definimos la funcion
def altura(x):
    return 1/(1 + x*x)
def Riemann(a,b,n,f):
    #p corresponde a las particiones -> Delta x
    p = (b-a)/n
   #Iniciamos la suma del area en 0
    A = 0
    #Usamos un for loop para realizar la suma de areas
    for i in range (n+1):
        A  += p*f(p/2 + i*p)
    #Retornamos el area total
    return A
#Probamos con n = 10000
aprox= Riemann(0,1,10000,altura)
print(4*aprox)




