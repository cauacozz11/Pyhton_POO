from modelos.restaurante import Restaurante

restaurante_praca  = Restaurante("tia Neide", "Italiano")
# restaurante_praca.receber_avaliacao('Cauã', 10)
# restaurante_praca.receber_avaliacao('Maria Eduarda', 10)
# restaurante_praca.receber_avaliacao('Marcos', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()