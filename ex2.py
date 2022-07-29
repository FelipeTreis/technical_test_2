'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''
n1 = 0
n2 = 1
n3 = 0

print('-Sequência de Fibonacci-')

insert_number = int(input('Insira um número: '))

while insert_number > n3:
   n3 = n1 + n2
   n1 = n2
   n2 = n3

if insert_number == 0 or insert_number == 1:
   print(f'O número {insert_number} pertence à sequência de Fibonacci.')

elif insert_number == n3:
   print(f'O número {insert_number} pertence à sequência de Fibonacci.')
   
else:
   print(f'O número {insert_number} não pertence à sequência de Fibonacci.')
