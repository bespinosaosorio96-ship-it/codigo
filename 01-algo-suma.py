"""
Algoritmo de la suma
Diseñe un algoritmo y un programa que sume dos numeros.

Entrada: a, b : 2 números
Proceso: realizar la suma de a y b
Salida: la suma de a y b

Algoritmo:
Inicio
    leer a y b
    c <- a + b
    escribir "la suma de a y b es: " c
Fin
"""

a = float(input("Ingrese primer numero: "))
b = float(input("Ingrese segundo numero: "))
c = a + b
print("La suma de", a, "y", b, "es:", c)
