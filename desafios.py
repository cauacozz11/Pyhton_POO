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




class ClienteBanco:
    lista = []
    def __init__(self, titular, saldo, sexo, idade, pais):
        self.titular = titular
        self.saldo = saldo
        self.sexo = sexo
        self.idade = idade
        self.pais = pais
        ClienteBanco.lista.append(self)
        
    @classmethod
    def listagem(cls):
        for i in cls.lista:
            print(f"Nome: {i.titular} | Saldo: {i.saldo} | Sexo: {i.sexo} | Idade: {i.idade} | País: {i.pais}")    




pessoa1 =ClienteBanco("Marcos", 123456, "Masculino", 34, "Brasil")
pessoa2 = ClienteBanco("Ana Clara", 987654, "Feminino", 28, "Brasil")
pessoa3 = ClienteBanco("Liam Smith", 112233, "Masculino", 40, "Estados Unidos")
pessoa4 = ClienteBanco("Sofia Rossi", 445566, "Feminino", 31, "Itália")
pessoa5 = ClienteBanco("Kenji Tanaka", 778899, "Masculino", 25, "Japão")




ClienteBanco.listagem()