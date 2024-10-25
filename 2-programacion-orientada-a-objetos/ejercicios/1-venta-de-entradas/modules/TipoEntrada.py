from .Entrada import *
class Infante(Entrada):
    def __init__(self, responsable: str):
        super().__init__('Infante', 3000)
        self.responsable = responsable
    def __str__(self) -> str:
        return super().__str__() + f" Responsable: {self.responsable}"
        
class Adulto(Entrada):
    def __init__(self):
        super().__init__('Adulto', 5000) 
    def __str__(self) -> str:
        return super().__str__()       
        
class AdultoMayor(Entrada):
    def __init__(self):
        super().__init__('AdultoMayor', 3500)
    def __str__(self) -> str:
        return super().__str__()      