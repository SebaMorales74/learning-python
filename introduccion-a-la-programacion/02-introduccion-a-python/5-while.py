while "condicion":
    "hacer algo"

"""
Los bucles son una parte fundamental de la programación, ya que nos permiten
repetir una acción un número determinado de veces. En Python, los bucles se
realizan con la instrucción while y for.

La instrucción while se utiliza para repetir un bloque de código mientras una
condición sea verdadera.

Aquí un ejemplo de un bucle infinito con una variable de control:
"""

bandera = True
while bandera:
    print("Este mensaje se imprimirá mientras la bandera sea verdadera")
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "n":
        bandera = False
    else:
        pass

"""
El bucle anterior imprimirá el mensaje "Este mensaje se imprimirá mientras la
bandera sea verdadera" mientras la variable bandera sea True. La variable
bandera se vuelve falsa cuando el usuario ingresa la letra "n".

Aquí el bucle se controla a través de la variable bandera, pero también se
puede controlar el bucle con la palabra reservada break, que se utiliza para
salir del bucle, o con la palabra reservada continue, que se utiliza para
saltar la iteración actual y continuar con la siguiente.

Aquí un ejemplo de un bucle infinito con la palabra reservada break:
"""

while True:
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "n":
        break
    else:
        print("Este mensaje se imprimirá mientras la opción sea diferente de n")

"""
En este bucle, la palabra reservada break se utiliza para salir del bucle
cuando el usuario ingresa la letra "n".

Aquí un ejemplo de un bucle infinito con la palabra reservada continue:
"""

while True:
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "n":
        break
    else:
        print("Este mensaje se imprimirá mientras la opción sea diferente de n")
        continue

"""
En el bucle anterior, la palabra reservada continue se utiliza para saltar la
iteración actual y continuar con la siguiente cuando el usuario ingresa la
letra "n".

Esto es distinto a la palabra reservada break, que se utiliza para
salir del bucle.

En resumen, los bucles while se utilizan para repetir un bloque de código
mientras una condición sea verdadera. Los bucles se pueden controlar con la
variable de control, la palabra reservada break y la palabra reservada
continue.
"""