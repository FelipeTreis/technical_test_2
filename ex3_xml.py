'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''
import xml


x = open('/home/felipe/technical_test_2/data.xml')

data = xml.load(x)

larger = 0
smaller = 0
sum1 = 0
media = 0
aux = 0

for dia in data:
    if (dia['valor']) != 0:
        aux = dia['valor']

        if aux > larger:
            larger = aux
        
        if smaller == 0:
            smaller = aux
        
        elif aux < smaller:
            smaller = aux

        sum1 += dia['valor']

print(f'O menor valor de faturamento do mês foi de: {smaller}.')
print(f'O maior valor de faturamento do mês foi de: {larger}.')

media = sum1 / len(data)
billing_days = ''

for i in data:
    if (i['valor']) != 0:

        if (i['valor']) > media:
            billing_days += i['dia'] + ' '

print(f'Dias em que o faturamento foi maior que a média mensal: {billing_days}')
