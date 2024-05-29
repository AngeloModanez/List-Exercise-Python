P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a Razão: '))
Q = int(input('Digite a quantidade de termos: '))
Termos = []
i = 0
while i < Q:
    Termos.append(P)
    P = P + R
    i += 1
print('\nLista resultante')
print(Termos)
