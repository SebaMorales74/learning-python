"""
1. Calcular la media de tres números pedidos por teclado.

Requisitos para solucionar el problema:
    - Debemos de saber cómo calcular la media de una cantidad determinada de números.
    - Pedir números por teclado.
    
¿Qué es una media o promedio?
https://es.wikipedia.org/wiki/Promedio

El tipo más común de promedio es la media aritmética.
Si se dan n números, cada número denotado por ai (donde i = 1,2, ..., n), la media aritmética es la suma de a dividida por n o.
La media aritmética, a menudo simplemente llamada la media, de dos números, como 2 y 8,
se obtiene al encontrar un valor A tal que 2 + 8 = A + A. Uno puede encontrar que A =   (2 + 8) / 2 = 5)
Cambiar el orden de 2 y 8 para leer 8 y 2 no cambia el valor resultante obtenido para A.

La media 5 no es menor que el mínimo 2 ni mayor que el máximo   8)
Si aumentamos el número de términos en la lista a 2, 8 y 11,
la media aritmética se encuentra resolviendo el valor de A en la ecuación 2 + 8 + 11 = A + A + A.
Uno encuentra que A = (2 + 8 + 11) / 3 = 7).

Analisis del problema:
    - Definir la media sin ningún valor asignado.
    - Debemos de recolectar 3 números.
    - Debemos de sumar los 3 números.
    - Debemos de dividir la media por 3.

Funciones a utilizar:
    - float()
    - int()
    - input()
    - print()
"""

# Resolución 1
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
media = (num1 + num2 + num3) / 3
print(f"El valor de la media es: {media}")

# Resolución 2
cantidadNumeros = int()
suma = int()
while cantidadNumeros > 3:
    numero = float(input(f"Ingresa el N°{cantidadNumeros + 1}: "))
    suma += numero
print(f"El valor de la media es: {suma/cantidadNumeros}")

# Resolución 3
suma = int()
for i in range(3):
    numero = float(input(f"Ingresa el N°{i + 1}: "))
    suma += numero
print(f"El valor de la media es: {suma/3}")