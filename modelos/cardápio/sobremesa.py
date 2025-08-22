from modelos.cardápio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    
    def __init__(self, nome, preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao
        
    def __str__(self):
        return f'Nome: {self._nome} | Preço: {self._preco} | Tamanho: {self._descricao}'
        
    def add_desconto(self):
        self._preco -= (self._preco * 0.03)
        
            
        
        
            