class Banco:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self._saldo = saldo
        self.__senha = senha
        self.opcao = None
        
    def decisao(self):
        print("Esolha uma opção: \n1 - Vizualizar as informações da sua conta\n2 - Depositar dinheiro\n3 - Sacar dinheiro: ") 
        decisão = int(input('Digite o número da sua escolha: '))
        while True:
            if decisão not in (1,2,3):
                print("Essa decisão não é válida!")
            else:
                self.opcao = decisão
                break
            
            decisão = int(input('Digite o número da sua escolha: '))
        
    
    def conta(self):
        if self.opcao == 1:
            print(f'informações da sua conta | Nome: {self.titular} | Saldo: {self.sa}')
           
   
   
nome = str(input('Digite seu nome: '))
saldo = float(input('Digite o saldo da sua conta: '))
senha = str(input('Digite a sua senha: '))        

usu1 = Banco(nome, saldo, senha) 

usu1.decisao()
usu1.conta()