# class Carro:
#     def __init__(self, modelo, cor , ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
 
# carro1 = Carro("Peugeot 208", "Prata", 2025)
# carro2 = Carro("Hrv", "Preto", 2020)
# carro3 = Carro("Porsche 911 Turbo", "Azul", 2025)        



# class Restaurante:
    
#     def __init__(self, nome, categoria, ativo = False, cidade = "São Paulo", ano_de_fundação = 2010):
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = ativo
#         self.cidade = cidade
#         self.ano_de_fundação = ano_de_fundação
        
#     def __str__(self):
#         return f"O nome do restaurante é {self.nome} e sua categoria é {self.categoria}"    
        
# restaurante1 = Restaurante("Don Carlo", "Espanhol")


# print(restaurante1)        
    
    
    
class Cliente:
    def __init__(self, nome, sexo, idade, nacionalidade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.nacionalidade = nacionalidade
        
cliente1 = Cliente("Marcos" , "Masculino", 32, "Brasileiro")
cliente2 = Cliente("Luana", "Feminino", 19, "Argentina")
cliente3 = Cliente("Maria Eduarda", "Feminino", "Brasileira" )        