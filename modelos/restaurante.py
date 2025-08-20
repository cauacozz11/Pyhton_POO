from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
         
    def __str__(self):
        return f"{self._nome} | {self._categoria} | {self.media_avaliacao()}" 
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)} | Avaliação: ")
        for i in cls.restaurantes: 
            print(f"{i._nome.ljust(25)} | {i._categoria.ljust(25)} | {i.chiclete.ljust(25)} | {i.media_avaliacao}")
            
    @property
    def chiclete(self):
        return "Em atividade" if self._ativo else "Não está em atividade"         
       
    def alternar_estado(self):
        self._ativo = not self._ativo  
        
    def receber_avaliacao(self, cliente, nota):
        if 2 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    @property   
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media    