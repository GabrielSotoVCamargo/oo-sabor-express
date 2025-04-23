class Pessoa:
    pessoas = [] # Lista de pessoas
    #metodo construtor

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)
    # Método especial para representar a pessoa como string

    # Adiciona a pessoa à lista de pessoas
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}'
    # Método de classe para listar todas as pessoas 
    @classmethod   
    def listar_pessoas(cls):
        print(f'{"Nome".ljust(20)} | {"Idade".ljust(10)} | {"Profissão"}')
        for pessoa in cls.pessoas:
            print(f'{pessoa.nome.ljust(20)} | {str(pessoa.idade).ljust(10)} | {pessoa.profissao}')
    # Método para retornar a saudação da pessoa
    @property
    def saudacao(self):
        # Ajusta o artigo definido "um" ou "uma" com base na profissão
        artigo = "uma" if self.profissao.lower().endswith('a') else "um"
        return f'Parabéns você é {artigo} {self.profissao}'
    # Método para aumentar a idade da pessoa
    def aumentar_idade(self, anos):
        self.idade += anos
    # Método para aumentar a idade da pessoa em 1 ano
    def aniversario(self):
        self.idade += 1

# Criação de instâncias da classe Pessoa
pessoa1 = Pessoa('João', 30, 'Engenheiro')
pessoa2 = Pessoa('Maria', 25, 'Médica')

# Listando todas as pessoas
Pessoa.listar_pessoas()

# Exibindo informações das pessoas
print('----------------------------------------')
print(pessoa1.saudacao)  # Exibindo a saudação da pessoa
print(pessoa2.saudacao)  # Exibindo a saudação da pessoa
print('----------------------------------------')
# Aumentando a idade da pessoa em 1 anos
pessoa1.aniversario()

