from modelos.restaurante import Restaurante
from modelos.cardápio.bebida import Bebida
from modelos.cardápio.prato import Prato
from modelos.cardápio.sobremesa import Sobremesa

restaurante_praca  = Restaurante("tia Neide", "Italiano")
bebida_suco = Bebida('Maracuja', 10, "Gande")
bebida_suco.add_desconto()
prato_pao = Prato('Pão com pomada', 5, 'Você come todo dia e não enjoa')
prato_pao.add_desconto()
sobremes_pet = Sobremesa('Petit gâteau', 20, "Um caldo de chocolate que apaixona!")
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_pao)
restaurante_praca.add_no_cardapio(sobremes_pet)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()