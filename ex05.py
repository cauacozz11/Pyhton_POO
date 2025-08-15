class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}"
    
    
    @property
    def saudacao(self):
        if self.profissao:
            return f"Olá, me chamo {self.nome} e sou {self.profissao}"
        else:
            return f"Olá, me chamo {self.nome}"   
    
    
    
    
    
    def aniversario(self):
        self.idade = self.idade + 1
        


pessoa1 = Pessoa("Cauã", 18, "Engenheiro de Software")
pessoa2 = Pessoa("Maria Eduarda",19, "Clínica geral", )  
pessoa3 = Pessoa("Marlene", 56, "Diretora escolar")

print("Imprimindo informações pessoais:")
print("-" *30)
print(pessoa1)
print("----")
print(pessoa2)
print("----")
print(pessoa3)      
print("----")

pessoa1.aniversario()
pessoa2.aniversario()



print("Exibindo informações após o aniverário: ")
print("-" *30)
print(pessoa1)
print("----")
print(pessoa2)
print("----")