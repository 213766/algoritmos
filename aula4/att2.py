valorPassagem = float(input("Valor da Passagem: "))
qtd = int(input("Quantidade de passagens compradas: "))

if qtd <= 50:
    valor = valorPassagem * 0.6 * qtd
else:
    valor = valorPassagem * 0.6 * 50
    qtd = qtd - 50
    valor += valorPassagem * qtd

valor = round(valor,2)

print(f'valor total é {valor}')