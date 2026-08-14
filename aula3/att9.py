valor = float(input("Insira o valor anual Recebido: "))

def calcularImposto(valor, base, taxa):
    if valor > base:
        imposto = (valor - base) * taxa
    return imposto

if valor > 44918.28:
    imposto = calcularImposto(valor,44918.28,0.275)
if valor > 35948.41:
    imposto = imposto + calcularImposto(valor,35948.41,0.225)
if valor > 26961.01:
    imposto = imposto + calcularImposto(valor,26961.01,0.15)
if valor > 17989.81:
    imposto = imposto + calcularImposto(valor,17989.81,0.075)

print(imposto)