def pegarNotas(valorReais, valorNota):
    valor = valorReais
    notas = 0
    while valor >= valorNota:
        notas = notas +  1
        valor -= valorNota

    return notas

def ajustarValor(valorReais, nrNotas, valorNotas):
    return valorReais - (nrNotas * valorNotas)

valor = float(input("Insira um valor em reais: "))
valorOG = valor

notas100 = pegarNotas(valor,100.0)
valor = ajustarValor(valor,notas100,100.0)

notas50 = pegarNotas(valor,50.0)
valor = ajustarValor(valor,notas50,50.0)

notas20 = pegarNotas(valor,20.0)
valor = ajustarValor(valor,notas20,20.0)

notas10 = pegarNotas(valor,10.0)
valor = ajustarValor(valor,notas10,10.0)

notas5 = 0
if valor % 2 != 0:
    notas5 = pegarNotas(valor,5.0)
    valor = ajustarValor(valor,notas5,5.0)

notas2 = pegarNotas(valor,2.0)
valor = ajustarValor(valor,notas2,2.0)

if valor > 0:
    print('valor não pode ser pago')
else:
    print(f"Para o valor de {valorOG} são necessárias {notas100} notas de 100, {notas50} notas de 50, {notas20} notas de 20, {notas10} notas de 10, {notas5} notas de 5 e {notas2} notas de 2.")