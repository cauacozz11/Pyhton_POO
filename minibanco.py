from time import sleep
class Banco:
    def __init__(self, titular, saldo, senha):
        self._titular = titular
        self._saldo = saldo
        self.__senha = senha
        self._opcao = None
        
    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo}"
    
    def escolha(self):
        while True:
            print("BEM VINDO AO BANCO")
            print()
            print("Opção de ações:")
            print()
            print("1 - Ver informações da conta\n2 - Ver saldo da conta\n3 - Sair do programa")
            self._opcao = int(input('Digite sua opção: '))
            print("-"* 30)
            if self._opcao == 1:
                sleep(0.5)
                print(self)
                sleep(0.5)
            if self._opcao == 2:
                print(f"Seu saldo é de R${self._saldo}")
                print('1 - Para depositar\n2 - Para sacar\n3 - Para sair: ')
                saldo2 = int(input('Sua escolha:'))
                if saldo2 == 1:
                    valor = int(input('Informe o valor para depositar: '))
                    self._saldo =   valor + self._saldo
                    print(f'Saldo atual: {self._saldo}')
    
 
 
usuario1  = Banco("Marcos", 12567, "lakhbbsysmdd8d664n")

usuario1.escolha()