class Musica:
    nome = ''
    artista = ''
    duração = float
    
musica_1 = Musica()
musica_1.nome = "Fallin in Love"
musica_1.artista = "Michael Pethery"
musica_1.duração = 3.34

musica_2 = Musica()
musica_2.nome = "Spike in my heart" 
musica_2.artista = "Dlevin Omyter"
musica_2.duração = 2.56

musica_3 = Musica()
musica_3.nome = "4zr"
musica_3.artista = "Blackoutz"
musica_3.duração = 4.01


lista = [musica_1, musica_2, musica_3]

print(vars(musica_2))   