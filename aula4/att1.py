cod = int(input('Insira o codigo do item: '))
qtd = int(input('Insira a quantidade solicitada: '))

match cod:
    case 10:
        valor = qtd * 1.1
    case 11:
        valor = qtd * 1.3
    case 12:
        valor = qtd * 1.5
    case 13:
        valor = qtd * 1.1
    case 14:
        valor = qtd * 1.3
    case 15:
        valor = qtd * 1.5

print(valor)