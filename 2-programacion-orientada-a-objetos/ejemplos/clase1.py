class Persona:
    def __init__(self,rut,nombre,genero,fecha_de_nacimiento):
        self.rut = rut
        self.nombre = nombre
        self.genero = genero
        self.fecha_de_nacimiento = fecha_de_nacimiento
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y mi fecha de nacimiento es el {self.fecha_de_nacimiento}")

bryanVallejos = Persona("21559135-2","Bryan Vallejos","Masculino","05 de abril 2004")
manuelMontecinos = Persona("21971639-7","Manuel Montecinos","Masculino","04 de noviembre del 2005")

bryanVallejos.saludar()
manuelMontecinos.saludar()
