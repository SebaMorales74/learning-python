# while "Mientras que"
# Realizar una acción hasta que esto no se cumple
realizarBucle = True
while realizarBucle == True:
    terminarElBucle = input("¿Quieres terminar el bucle? [y/N]: ")
    if terminarElBucle == "Y" or terminarElBucle == "y":
        print("Adios mundo cruel..")
        realizarBucle = False
    else:
        print("Gracias por salvarme ✨")

# Pero tambien puedo generar bucles infinitos sin la necesidad
# De cambiar el estado que está comprobando el while
while True:
    terminarElBucle = input("¿Quieres terminar el bucle? [y/N]: ")
    if terminarElBucle == "Y" or terminarElBucle == "y":
        print("Adios mundo cruel..")
        break
    else:
        print("Gracias por salvarme ✨")

# Repetir una cantidad de veces alguna acción
# Por ejemplo, imprimir 10 veces la palabra "Hola" en la terminal
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")
print("Hola")

# Contador que imprime "Hola" 10 veces
contador = 0
while True:
    if contador == 10:
        break

    print("Hola", contador)
    contador += 1 # Es una simplificación de: contador = contador + 1

# Cómo recomendación, si necesitan fabricar bucles
# Hasta una posición en especifico, debes de utilizar
# for a in range(comienzo,parada,paso)
for posicion in range(0,10,1):
    print("Hola", posicion)

# Pero, for in es más que solo un contador
# Me permite evaluar individualmente o realizar algo por cada elemento que exista en este grupo de elementos.
palabra = input("Ingresa una palabra sin espacios: ")
tieneEspacios = False

for letra in palabra:
    if letra == " ":
        tieneEspacios = True
        break

if tieneEspacios == True:
    print("Existe un espacio en la palabra. Terminando el programa...")
elif tieneEspacios == False:
    print("La palabra no contiene espacios")