class Persona:
    def __init__(self, rut: int, nombre: str, apellido: str, email: str):
        self.__rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.email}"


cristian = Persona(21256946, 'Cristian', 'Lorca',
                   'cristian.lorca09@incapmail.cl')
cesar = Persona(21543678, 'Cesar', 'Silva', 'cesar.silva@incapmail.cl')
sebastian = Persona(21252515, 'Sebastian', 'Morales',
                    'sebastian.morales@incapmail.cl')

print(cristian)
print(cesar)
print(sebastian)

# <__main__.Persona object at 0x0000024A230D9F10>
