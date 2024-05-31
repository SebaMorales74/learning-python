"""
Pedir al usuario un numero entre 10 y 20, dar opcion para reingresar el dato
si no esta entre 10 y 20.

Una vez ingresado el numero, imprimir todos los numeros impares desde el
valor ingresado hasta 1.

1. Inisistir en un dato al usuario
2. Como determinar un numero impar
"""

while True:
    numero = int(input("Ingresa un numero entero entre 10 y 20: "))
    
    if numero > 10 and numero < 20:
        break
    else:
        continue

contador = 0
while contador < numero:
    contador += 1
    
    if (numero-contador) % 2 == 1:
        print(numero-contador)