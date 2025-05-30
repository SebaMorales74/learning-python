# Estructura de decisión o evaluación
# Esto yo lo útilizo para revisar si un hecho es verdadero o falso.
# Ej:
luzPrendida = False
if luzPrendida == False:
    print("La luz está apagada")

# Para realizar preguntas, yo poseo los operadores llamados
# "Operadores Lógicos"
# == "¿Es igual que?"
# < "¿Es menor que?"
# > "¿Es mayor que?"

a = int(input("Ingresa un número entero: "))
b = int(input("Ingresa otro número entero: "))

if a == b:
    print("Son iguales")

if a < b:
    print("A es menor que B")

if a > b:
    print("A es mayor que B")

# También poseemos operadores que cambian las reglas del juego
# Puedo preguntar totalmente lo contrario
# not "NO es [pregunta] que"

if not a == b:
    print("NO son iguales")

if not a < b:
    print("A NO es menor que B")

if not a > b:
    print("A NO es mayor que B")

# Si quisieramos controlar tanto si es que el hecho se cumple como si no
# Podemos ocupar
# else "Si cualquier otra cosa pasa"

if a == b:
    print("Son iguales")
else:
    print("No son iguales")

# No solo podemos hacer preguntas individualmente
# Si no, que podemos agruparlas con los operadores de "else if" y "else"
# De esa forma, nueva evaluación de decisiones puede preguntar
# if "Si es que esta cosa pasa"
# elif "Si es que esta otra cosa pasa"
# else "Si cualquier otra cosa pasa"
# Al utilizar esta estructura, la decisión se va a quedar con lo primero que pase

opcion = input("Ingresa una opción (1,2,3): ")

if opcion == "1":
    print("Presionaste la opción 1")
elif opcion == "2":
    print("Presionaste la opción 2")
elif opcion == "3":
    print("Presionaste la opción 3")
else:
    print("Opción invalida 😡😠")