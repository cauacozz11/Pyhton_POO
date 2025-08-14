class Musica:
    lista = []
    
    def __init__(self, nome, artista, duração):
        self.nome = nome
        self.artista = artista
        self.duração = int(duração)
        Musica.lista.append(self)
        
    def __str__(self):
        return f"{self.nome} | {self.artista} | {self.duração}"   
    

        
musica1 = Musica("Verão que chove" , "Fagundes", 2.23)

