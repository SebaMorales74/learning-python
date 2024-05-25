"""
2. Crear un algoritmo que muestre por pantalla el doble y el triple de un número 
ingresado por teclado.

Requisitos para solucionar el problema:
    - Multiplicación
    - Mostrar por pantalla.
    - Ingreso por teclado.
    - Concatenar.
    
Analisis del problema:
    - Pedir un número.
    - Multiplicar por 2 y por 3.
    - Mostrar por pantalla.
"""

num1 = int(input("ingrese un numero"))
print("el doble del numero es: ", (num1*2))
print("el triple del numero es:", (num1*3))

# Recomendada
num = int(input("Ingrese un numero: "))
print(f"El doble del numero es {num*2}\nEl triple del numero es {num*3}")