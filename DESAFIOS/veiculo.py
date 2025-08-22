from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo}'    
        
    @abstractmethod
    def ligar(self):
        pass    
    