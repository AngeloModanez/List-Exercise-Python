lstValores = []
valor = int(input('Digite um Inteiro: '))
while valor != 0:
    lstValores.append(valor)
    valor = int(input('Digite um Inteiro: '))
print('\nResultado:')
print(lstValores)
print(f'A lista comtem {len(lstValores)} elementos!')
print('Fim da Execuçãog')