class carro:
    modelo = '' 
    marca = ''
    ano = int

# metodo construtor
    def __init__ (self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca 
        self.ano = ano
# metodo para exibir detalhes do carro
    def exibir_detalhes(self):
        print(f'Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}')
# metodo para calcular a idade do carro    
    def idade(self):
        return 2023 - self.ano
    
# Informações / dados de carro
carro1 = carro(modelo='Fusca', marca='Volkswagen', ano=1970)

# objeto carro1 chama o metodo exibir_detalhes
print('----------------------------------------')
carro1.exibir_detalhes()
print('----------------------------------------')
print(f'Idade do carro: {carro1.idade()} anos')
print('----------------------------------------')
    