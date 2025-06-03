class Musica:
    nome = ''
    artista = ''
    duracao = int

# Metodo construtor 
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

print(musica1.nome, musica1.artista, musica1.duracao)
print(musica2.nome, musica2.artista, musica2.duracao)
print(musica3.nome, musica3.artista, musica3.duracao)


