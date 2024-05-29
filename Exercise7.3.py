N = int(input('Digite a Quantidade de Itens: '))
L = []
for i in range(N):
    x = float(input(f'\tElemento {i}: '))
    L.append(x)
print('\nResultado:')
for valor in L:
    print(f'{valor:.2f}', end='\t')
print('Fim da Execução')
