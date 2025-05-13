# começei a fazer o metodo de listar 
numeros = []
# Loop para solicitar 5 números ao usuário
for i in range(5):
    numero = int (input(f'Digite um número {i + 1}: '))
    numeros.append(numero) # Adiciona o número à lista
# print dos numeros digitados além de mostrar o maior e menor número e a soma dos números
print('Números digitados:', numeros)
print('Maior número:', max(numeros))
print('Menor número:', min(numeros))
print('Soma dos números:', sum(numeros))


