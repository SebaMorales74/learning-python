from .Cliente import *
from .TipoEntrada import *
from .Vendedor import *


class Venta:
    def __init__(self, vendedor: Vendedor, cliente: Cliente, entradas: list, total: int):
        self.vendedor = vendedor
        self.cliente = cliente
        self.entradas = entradas
        self.total = total

    def obtenerEntradas(self) -> str:
        entradas = ""
        for entrada in self.entradas:
            entradas += f"{entrada}\n"
        return entradas
    
    def __str__(self) -> str:
        return f"{self.vendedor} {self.cliente} {self.obtenerEntradas()} Total: {self.total}"
