def lerElementos(nrElementos: int):
    elementos = []
    for i in range(nrElementos):
        elementos.append(input(f'Insira o elemento {i}: '))
    return elementos

tamanhoListas = 10
listaFinal = []

listaA = lerElementos(tamanhoListas)
listaB = lerElementos(tamanhoListas)

for i in range(tamanhoListas):
    listaFinal.append(listaA[i])
    listaFinal.append(listaB[i])

print(listaFinal)