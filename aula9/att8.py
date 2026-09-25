def isNumeric(num):
    try:
        float(num)
        return True
    except:
        return False

def adicionarItem(lista, item):
    if isNumeric(item):
        lista.append(float(item))
    else:
        print('Nao é numero')

def exibirItens(lista):
    for n in lista:
        print(n)

def calcularSoma(lista):
    return sum(lista)

def calcularMaior(lista):
    return max(lista)

lista = []

print("Selecione uma opção:")

while True:

    opcao = input("").lower()

    if opcao not in ["a","b","c","d","x"]:
        print("Selecione uma opção válida.")
        continue

    match opcao:
        case "x":
            break
        case "a":
            item = input("Item para adicionar: ")
            adicionarItem(lista, item)
        case "b":
            exibirItens(lista)
        case "c":
            print(calcularSoma(lista))
        case "d":
            print(calcularMaior(lista))