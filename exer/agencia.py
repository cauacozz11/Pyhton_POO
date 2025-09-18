from heranca import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero
    
    def __str__(self):
        return f'Nome: {self._nome} | Endereço: {self._endereco} | Número: {self._numero}'
    
    
ag = Agencia('C6', 'Rua 13 de Maio', 1611)

print(ag)    