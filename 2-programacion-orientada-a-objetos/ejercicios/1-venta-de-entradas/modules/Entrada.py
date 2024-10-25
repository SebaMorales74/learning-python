class Entrada:
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio
    def __str__(self) -> str:
        return f"Entrada: {self.nombre} ${self.precio}"