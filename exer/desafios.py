# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo = False
        
#     def __str__(self):
#         return f"Titular: {self.titular} | Saldo: {self.saldo}"
    
    
#     @classmethod
#     def ativar_conta(cls, conta):
#         conta._ativo = True
        
        


# pessoa1 = ContaBancaria("Cauã", 67000)  
# pessoa2 = ContaBancaria("Maria Eduarda", 89000)  

# print(pessoa1)
# print(pessoa2)

# print(f"Antes de ativar -  Ativo = {pessoa1._ativo}")
# print(f"Antes de ativar -  Ativo = {pessoa2._ativo}")
# print()
# ContaBancaria.ativar_conta(pessoa1)
# print(f"Depois de ativar - Ativo = {pessoa1._ativo}")
# print(f"Depois de ativar - Ativo = {pessoa2._ativo}")



# class ContaBancPythonica:
#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False
        
        
#     @property
#     def titular(self):
#         return self._titular
    
    
#     @property
#     def saldo(self):
#         return self._saldo
    
    
#     @property
#     def ativo(self):
#         return self._ativo   
    
    
    
# conta4  = ContaBancPythonica("Maricota", 30456789)

# print(conta4.titular)
# print(conta4.saldo)
# print(conta4.ativo)     




# class ClienteBanco:
#     lista = []
#     def __init__(self, titular, saldo, sexo, idade, pais):
#         self.titular = titular
#         self.saldo = saldo
#         self.sexo = sexo
#         self.idade = idade
#         self.pais = pais
#         ClienteBanco.lista.append(self)
        
#     @classmethod
#     def listagem(cls):
#         for i in cls.lista:
#             print(f"Nome: {i.titular} | Saldo: {i.saldo} | Sexo: {i.sexo} | Idade: {i.idade} | País: {i.pais}")    




# pessoa1 =ClienteBanco("Marcos", 123456, "Masculino", 34, "Brasil")
# pessoa2 = ClienteBanco("Ana Clara", 987654, "Feminino", 28, "Brasil")
# pessoa3 = ClienteBanco("Liam Smith", 112233, "Masculino", 40, "Estados Unidos")
# pessoa4 = ClienteBanco("Sofia Rossi", 445566, "Feminino", 31, "Itália")
# pessoa5 = ClienteBanco("Kenji Tanaka", 778899, "Masculino", 25, "Japão")




# ClienteBanco.listagem()


class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicação):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicação = ano_publicação
        self._disponivel = True
        Livro.livros.append(self)
        
    def __str__(self):
        return f"Título: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicação} | Disponibilidade: {self._disponivel}"
    
    def emprestar(self):
        self._disponivel = False
        
    @staticmethod
    def livros_ano(ano):
        lista_livros_dispo = []
        for i in Livro.livros:
            if i._ano_publicação == ano and i._disponivel:
                lista_livros_dispo.append(i)
        if lista_livros_dispo:        
            print(f'Os livros disponíveis no ano de {ano} são: ')        
            for i in lista_livros_dispo:
                print(f'{i._titulo}')
        else:
            print(f'Não existe nenhum livro do ano de {ano} cadastrado')            
        
  

# livro1 = Livro("Amor que mata", "José Garmalhozo", 2006)
# livro2 = Livro("Histórias do Mundo", "Ana Paula", 2006)
# livro3 = Livro("Python Fácil", "Carlos Silva", 2020)  
# livro3.emprestar()
# Livro.livros_ano(2020)