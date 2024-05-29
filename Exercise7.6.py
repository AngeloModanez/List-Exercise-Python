lstValores = []
valor = int(input('Digite um Inteiro: '))
while valor != 0:
    if valor not in lstValores:
        lstValores.append(valor)
    else:
        print(f'ERROR. O valor {valor} já está na lista!')
    valor = int(input('Digite um Inteiro: '))
print('\nResultado:')
print(lstValores)
print(f'A lista comtem {len(lstValores)} elementos!')
print('Fim da Execução')