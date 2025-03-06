class musica:
    nome = ''
    artista = ''
    duracao = int

rock_musica = musica()
rock_musica.nome = 'I Was Made for Lovin’ You'
rock_musica.artista = 'Paul Stanley'
rock_musica.duracao = 359

musicas = [rock_musica]

print(vars(rock_musica))