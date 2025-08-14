class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca  = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"
restaurante_praca.ativo = True


restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
restaurante_pizza.ativo = True

# if restaurante_pizza.categoria == "Fast Foode":
#     print('isso ai')
# else:
#     print('não é isso ai')    

# if restaurante_pizza.ativo:
#     print("O restaurante está ativo")
# else:    
#     print("O restaurante está inativo")
    
# categoria = Restaurante.categoria 

# print(categoria)   


restaurante_praca.nome = "Bistrô"

print(f"O nome do restaurante é {restaurante_praca.nome} e sua categoria é {restaurante_praca.categoria} ")