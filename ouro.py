class Pessoa():
    def __init__(self, nome,idade,email,celular):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__celular = celular
        
        @property
        def nome(self):
            return self.__nome
        
        @nome.setter
        def nome(self,novo_nome):
            self.__nome = novo_nome
            
        @property
        def idade(self):
            return self.__idade
        
        @idade.setter
        def idade(self, nova_idade):
            if nova_idade < 0:
                print('Idade não pode ser negativa')
            else:
                self.__idade = nova_idade        
                        
        @property
        def email(self):
            return self.__email
        
        @email.setter
        def email(self, novo_email):
            self.__email = novo_email
            
        @property
        def celular(self):
            return self.__celular
        
        @celular.setter
        def celular(self, novo_celular):
            self.__celular = novo_celular    
            
            
        def exibir_dados(self):
            print('Exibir')
            print(f'Nome: {self.__nome}')
            print(f'Nome: {self.__idade}')    
            print(f'Nome: {self.__email}')        
            print(f'Nome: {self.__celular}')    
            
            
nome = input('Digite o nome de uma pessoa: ')
idade = int(input('Didite a idade da pessoa: ')) 
email = input('Digite o email da pessoa: ')
celular = input('Digite o celular da pessoa: ')  

#Criando objeto da pessoa
p1 = Pessoa(nome,idade,email,celular)
p1.nome = nome
p1.idade = idade
p1.email = email
p1.celular = celular

p1.exibir_dados()   