N = int(input('Digite a Quantidade: '))
lPo = []
lNe = []
for i in range(N):
    X = int(input(f' Elemento {i} >>\t'))
    if X >= 0:
        lPo.append(X)
    else:
        lNe.append(X)
print(f'Lista Negativa: {lNe}, contém: {len(lNe)} elementos')
print(f'Lista Positiva: {lPo}, contém: {len(lPo)} elementos')
