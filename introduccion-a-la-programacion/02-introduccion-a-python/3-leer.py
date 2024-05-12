input()

"""
En Python podemos leer datos desde la consola utilizando la función input(),
esta función nos permite leer cadenas de texto y números enteros.

Por defecto, input() lee cadenas de texto, por lo que si queremos leer un número
entero debemos de convertir la entrada a un número entero.

Por ejemplo:
"""

# Leer un número entero
entero = int(input("Ingresa un número entero: "))

# Leer un número flotante
real = float(input("Ingresa un número flotante: "))

# Leer una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Leer un valor booleano
bandera = bool(input("Ingresa un valor booleano (True/False): "))

"""
Tenemos que tener en cuenta que la función input() siempre devuelve una cadena de texto,
y no podemos restringir el tipo de dato que se ingresa, por lo que debemos de validar
el tipo de dato que se ingresa.

Por ejemplo, si queremos leer un valor booleano, debemos de validar que el valor ingresado
sea "True" o "False", y convertirlo a un valor booleano.

Esto lo realizamos ya que en caso de que el valor no corresponde a un valor compatible
con el tipo de dato que esperamos, Python nos arrojará un error.
"""