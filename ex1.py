'''
Observe o trecho de código abaixo:

	int INDICE = 13, SOMA = 0, K = 0;

	enquanto K < INDICE faça
	{
		K = K + 1;
		SOMA = SOMA + K;
	}

	imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
'''

index = 13
sum = 0
k = 0

for k in range(index):
    if k < index:
        k = k + 1
        sum = sum + k

    print(sum)
