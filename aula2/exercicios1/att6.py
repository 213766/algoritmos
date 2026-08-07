VALOR_P = 10.0
VALOR_M = 12.0
VALOR_G = 15.0

def getQtd(tamanho: str):
    return int(input(f'Insira a quantidade de camisa(s) tamanho {tamanho} vendidas: '))

qtdP = getQtd('P')
qtdM = getQtd('M')
qtdG = getQtd('G')

valorVendaP = qtdP * VALOR_P
valorVendaM = qtdM * VALOR_M
valorVendaG = qtdG * VALOR_G

valorVenda = valorVendaP + valorVendaM + valorVendaG

print(valorVenda)