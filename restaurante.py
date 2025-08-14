class Restaurante:
    restaurantes = []
    
    def __init__(self, _nome, _categoria):
        self._nome = _nome.title()
        self._categoria = _categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f"{self._nome} | {self._categoria}" 
    
    def listar_restaurantes():
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for i in Restaurante.restaurantes: 
            print(f"{i.nome.ljust(25)} | {i.categoria.ljust(25)} | {i.ativo}")
            
    @property
    def ativo(self):
        return "Em atividade" if self._ativo else "Não está em atividade"         
       
        
restaurante_praca  = Restaurante("tia Neide", "Italiano")
restaurante_pizza = Restaurante("moskovia", "Russo")   


Restaurante.listar_restaurantes()