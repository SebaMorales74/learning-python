class Cliente:
    def __init__(self, rut: str, nombre: str, apellido: str, telefono: str, email: str) -> None:
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self) -> str:
        return f"Cliente: {self.nombre} {self.apellido}"
