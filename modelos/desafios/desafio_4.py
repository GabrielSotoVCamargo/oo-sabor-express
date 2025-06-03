class contabancariapyhonica:
       #metodo construtor
    def __init__(self, titular, saldo):
        self._titular= titular
        self._saldo = saldo 
        self._ativo = False
    #metodo construtor
    def __str__(self):
        return f'A Conta é do {self._titular} - Saldo: R${self._saldo}'
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo 

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    #metodo especial
conta1 = contabancariapyhonica('Joâo', 1000)
conta2 = contabancariapyhonica('Maria', 500)
#metodo especial
print(conta1)
print(conta2)
#     return conta
conta3 = contabancariapyhonica('Pedro', 2000)
print(f'Antes de ativar: conta ativa? {conta3._ativo}')
contabancariapyhonica.ativar_conta(conta3)
print(f'Depois de ativar: conta ativa? {conta3._ativo}')
#     return conta
conta4 = contabancariapyhonica('Ana', 1500)
print(f'Titular: {conta4.titular}')

class clientebanco:
    def __init__(self, nome, idade, profissao, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao 
        self.endereco = endereco 
        self.cpf = cpf

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = contabancariapyhonica(titular, saldo_inicial)
        return conta

conta_cliente1 = clientebanco.criar_conta('João', 1000)
print(f'Conta criada para {conta_cliente1.titular} com saldo inicial de R${conta_cliente1.saldo}')

client1= clientebanco('João', 30, 'Engenheiro', 'Rua A, 123', '123.456.789-00')
client2= clientebanco('Maria', 25, 'Médica', 'Rua B, 456', '987.654.321-00')
client3= clientebanco('Pedro', 40, 'Professor', 'Rua C, 789', '456.789.123-00')


        

    


    

        