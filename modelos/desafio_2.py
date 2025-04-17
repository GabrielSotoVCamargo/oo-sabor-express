class restaurante:
    nome = ''
    categoria = ''
    ativo = False
    capacidade = 0
    nota_avaliacao = 0.0
    #metodo construtor
    def __init__(self, nome, categoria, ativo, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
    
restaurante1 = restaurante(nome='Bistrô', categoria='Italiana', ativo=True, capacidade=50, nota_avaliacao=4.5)
restaurante2 = restaurante(nome='Pizza Place', categoria='Fast Food', ativo=True, capacidade=100, nota_avaliacao=4.0)

print(restaurante1.nome, restaurante1.categoria, restaurante1.ativo, restaurante1.capacidade, restaurante1.nota_avaliacao)
print(restaurante2.nome, restaurante2.categoria, restaurante2.ativo, restaurante2.capacidade, restaurante2.nota_avaliacao)

