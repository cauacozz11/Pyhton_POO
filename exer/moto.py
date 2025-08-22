from veivulo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome, modelo, tipo):
        super().__init__(nome,modelo)
        self._tipo = tipo
     
     
    def __str__(self):
        return f"{super().__str__() } | Tipo: {self._tipo}"    