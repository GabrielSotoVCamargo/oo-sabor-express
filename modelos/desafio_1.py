class carro:
    modelo = ''
    cor = ''
    ano = 0
#metodo construtor 
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
# Informações / dados de carro
carro1 = carro(modelo ='Fusca', cor='azul', ano=1970)
carro2 = carro(modelo ='Civic', cor='preto', ano=2020)
carro3 = carro(modelo ='corola', cor='preto', ano=2020)

print(carro1.modelo, carro1.cor, carro1.ano)
print(carro2.modelo, carro2.cor, carro2.ano)
print(carro3.modelo, carro3.cor, carro3.ano)