'''
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
- Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
- Evite usar funções prontas, como, por exemplo, reverse;
'''
word = input('Insira uma palavra: ')
crt = []
inverse = ''

for letter in word:
    crt.append(letter)

leng = len(crt) - 1

while leng >= 0:
    inverse += (crt[leng])
    leng -= 1

print(f"A palavra '{word}' invertida fica: {inverse}")