print()

"""
print() es una función que imprime/escribe en la consola, 
nos permite mostrar expresiones y mensajes en la terminal.

Por defecto, print() imprime en la consola un salto de línea

Todo lo que queramos mostrar en la consola lo debemos
de incluir dentro de los paréntesis de la función print().

Por ejemplo:
"""

print("Hola mundo!")

# Podemos insertar variables en la función print() de la siguiente manera:
variable = "valor"
print(variable)

# También podemos concatenar o imprimir varias variables o expresiones en una sola línea
nombre = "Sebastian"
print("Hola, como estas", nombre)

# Podemos imprimir variables y expresiones de diferentes tipos
edad = 25
print("Hola", nombre, "tienes", edad, "años")

"""
Existen varias formas de concatenar, por lo que te voy
a enseñar distintas formas de hacerlo y sus diferencias.

Esto es fundamental cuando trabajamos con print, ya que
nos permite mostrar mensajes y variables de forma más
legible y ordenada.
"""

"""
1. Concatenación con el operador +
En este caso, TODAS las variables deben ser del mismo tipo
y debes de explicitamente escribir los espacios y los signos
"""
print("Hola " + nombre + "! tienes " + str(edad) + " años")

"""
2. Concatenación con la función format()
La función format() nos permite concatenar variables de
diferentes tipos y nos permite formatear la salida.
"""
print("Hola {}! tienes {} años".format(nombre, edad))

"""
3. Concatenación con f-strings
Las f-strings son una forma más moderna de concatenar
variables y expresiones, es la forma más recomendada
para concatenar en Python. (Es mi favorita :3)
"""
print(f"Hola {nombre}! tienes {edad} años")

"""
4. Concatenación con %s
La concatenación con %s es una forma antigua de concatenar
variables y expresiones, no es recomendada usarla.
Puede ser confusa y no es tan flexible como las f-strings.
"""
print("Hola %s! tienes %s años" % (nombre, edad))