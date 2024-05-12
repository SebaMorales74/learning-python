if "condición1":
    "hacer algo si la condición es verdadera"
elif "condición2":
    "hacer algo si esta condición es verdadera"
else:
    "hacer algo si ninguna de las condiciones anteriores es verdadera"

"""
Las deciciones son una parte fundamental de la programación, ya que nos permiten
tomar decisiones en base a ciertas condiciones. En Python, las decisiones se
realizan con la instrucción if, elif y else.

Las deciciones se utilizan con los llamados operadores lógicos, que son los
siguientes:

== -> Igual a
!= -> Diferente a
> -> Mayor que
< -> Menor que
>= -> Mayor o igual que
<= -> Menor o igual que
and -> Y
or -> O
not -> No

La instrucción if se utiliza para evaluar una condición, si esta es verdadera
se ejecuta el bloque de código que se encuentra dentro de la instrucción if.

La instrucción elif se utiliza para evaluar otra condición, si la condición
anterior no se cumple, se evalúa la condición de elif, si esta es verdadera se
ejecuta el bloque de código que se encuentra dentro de la instrucción elif.

La instrucción else se utiliza para ejecutar un bloque de código si ninguna de
las condiciones anteriores se cumple.

Aquí un ejemplo de decición individual por cada operador lógico:
"""

valorIngresado = int(input("Ingrese un número: "))

if valorIngresado == 0:
    print("El número ingresado es igual a 0")

if valorIngresado != 0:
    print("El número ingresado es diferente a 0")
    
if valorIngresado > 0:
    print("El número ingresado es mayor a 0")
    
if valorIngresado < 0:
    print("El número ingresado es menor a 0")
    
if valorIngresado >= 0:
    print("El número ingresado es mayor o igual a 0")
    
if valorIngresado <= 0:
    print("El número ingresado es menor o igual a 0")

if valorIngresado > 0 and valorIngresado < 10:
    print("El número ingresado es mayor a 0 y menor a 10")
    
if valorIngresado > 0 or valorIngresado < 10:
    print("El número ingresado es mayor a 0 o menor a 10")
    
if not valorIngresado == 0:
    print("El número ingresado no es igual a 0")


"""
Aquí un ejemplo de decición múltiple:
"""    

if valorIngresado == 0:
    print("El número ingresado es igual a 0")
elif valorIngresado != 0:
    print("El número ingresado es diferente a 0")
elif valorIngresado > 0:
    print("El número ingresado es mayor a 0")
elif valorIngresado < 0:
    print("El número ingresado es menor a 0")
elif valorIngresado >= 0:
    print("El número ingresado es mayor o igual a 0")
elif valorIngresado <= 0:
    print("El número ingresado es menor o igual a 0")
elif valorIngresado > 0 and valorIngresado < 10:
    print("El número ingresado es mayor a 0 y menor a 10")
elif valorIngresado > 0 or valorIngresado < 10:
    print("El número ingresado es mayor a 0 o menor a 10")
elif not valorIngresado == 0:
    print("El número ingresado no es igual a 0")
else:
    print("El número ingresado no cumple con ninguna condición")
    
"""
La diferencia entre la decición individual y la decición múltiple es que en la
decición individual se evalúan todas las condiciones, mientras que en la
decición múltiple se evalúan las condiciones de arriba hacía abajo y se ejecuta
el bloque de código de la primera condición que se cumpla, ignorando las
condiciones restantes.

Esto debido a que si solo checamos con if, se ejecutarán todas las condiciones
que se cumplan, mientras que si usamos elif, se ejecutará la primera condición
que se cumpla y se ignorarán las demás.
"""