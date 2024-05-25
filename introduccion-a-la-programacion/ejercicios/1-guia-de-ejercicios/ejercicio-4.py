"""
4. Diseñar un algoritmo que calcule el volumen de un cilindro dados su radio y 
altura (primero el programa deberá verificar si son positivas). 

Requisitos para solucionar el problema:
    - Calcular el volumen de un cilindro.
    - Ingreso de datos.
    - Mostrar por pantalla.
    - Decisión.
    
Calcular el volumen de un cilindro:
    El volumen de un cilindro es π r² h, y el área de su superficie es 2π r h + 2π r².

Ingreso de datos:
    input() o si es numero int(input())

Mostrar por pantalla:
    print()

Decisión:
    if condicion:
        pass
    elif condicion:
        pass
    else:
        pass
"""

# Forma 1
import math
radio = int(input("Ingrese el radio del cilindro: "))
altura = int(input("Ingrese la altura del cilindro: "))
if radio < 0 or altura < 0:
    print("El radio y la altura deben de ser positivos.")
volumen = math.pi * (radio**2) * altura

# Forma 2
pi = float(3.14)
radio = int(input("Ingrese el radio del cilindro: "))
altura = int(input("Ingrese la altura del cilindro: "))
if radio < 0 or altura < 0:
    print("El radio y la altura deben de ser positivos.")
volumen = pi * (radio**2) * altura
print("El volumen del cilindro es:",volumen)