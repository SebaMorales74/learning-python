# Definir variables
variable = "valor"
variable = 12
variable = 12.5
variable = True
variable = False
variable = None

"""
En Python podemos definir variables de forma flexible, es decir,
podemos asignar cualquier tipo de valor a una variable.

Sin embargo, es importante tener en cuenta que una variable puede
cambiar de tipo de dato en cualquier momento, por lo que es importante
tener en cuenta el tipo de dato que se trabaja a una variable.

Gracias a las extensiones de Pylance y Python de Visual Studio Code,
podemos verificar el tipo de dato que se le asigna a una variable.

Al posicionar el cursor sobre una variable, podemos ver el tipo de dato
tal como se muestra en los siguientes ejemplos:
"""

# (variable) nombre: Literal['']
nombre = ""
# (variable) nombre: type[str]
nombre = str
# (variable) nombre: str
nombre = str()

# (variable) edad: Literal[25]
edad = 25
# (variable) edad: type[int]
edad = int
# (variable) edad: int
edad = int()

# (variable) estatura: Literal[1.75]
estatura = 1.75
# (variable) estatura: type[float]
estatura = float
# (variable) estatura: float
estatura = float()

# (variable) esVerdad: Literal[True]
esVerdad = True
# (variable) esVerdad: type[bool]
esVerdad = bool
# (variable) esVerdad: bool
esVerdad = bool()

# (variable) esFalso: Literal[False]
esFalso = False
# (variable) esFalso: type[bool]
esFalso = bool
# (variable) esFalso: bool
esFalso = bool()

# (variable) noExiste: Literal[None]
noExiste = None
# (variable) noExiste: type[None]
noExiste = None
# (variable) noExiste: None
noExiste = None