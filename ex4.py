'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora.
'''

def porcent(state, total):
    return round(((100*state) / total), 2)

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
other = 19849.53

total = sp + rj + mg + es + other

print(f'Porcentagem de faturamento no estado de SP: {porcent(sp ,total)}%.')
print(f'Porcentagem de faturamento no estado de RJ: {porcent(rj ,total)}%.')
print(f'Porcentagem de faturamento no estado de MG: {porcent(mg ,total)}%.')
print(f'Porcentagem de faturamento no estado de ES: {porcent(es ,total)}%.')
print(f'Porcentagem de faturamento em outros estados: {porcent(other, total)}%.')