
def adicionarItem(lista, item):
    if exists(lista,item):
        print(f"Item {item} já existe na lista.")
    lista.add(item)

def removerItem(lista, item):
    try:
        lista.remove(item)
    except:
        print(f"Item {item} não existe na lista.")

def exibirItens(lista):
    print(", ".join(lista))

def ordenarLista(lista):
    ordenado = []
    for item in lista:
        ordenado.append(item)
    ordenado.sort()
    return ordenado

def exists(lista, item):
    copia = lista.copy()
    try:
        copia.remove(item)
        return True
    except:
        return False

def salvarLista(lista):
    arquivo = open("./aula8/padrao lista.txt", "w")
    arquivo.write("\n".join(lista))

def lerLista():
    arquivo = open("./aula8/padrao lista.txt", "r")
    lista = set()
    for l in arquivo.readlines():
        lista.add(l.replace("\n", ""))

    return lista

def main():
    listaCompras = set()

    print("Selecione uma opção:")
    print("a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)\nb. remover item\nc. exibir todos os itens\nd. ordernar o conjunto alfabeticamente\ne. verificar se um item está contido em um conjunto\nf. gravar a lista de compras em um arquivo (padrao lista.txt)\ng. ler a lista de comprar de um arquivo (padrao lista.txt)\nx. finalizar lista.")

    while True:

        opcao = input("").lower()

        if opcao not in ["a","b","c","d","e","f","g","x"]:
            print("Selecione uma opção válida.")
            continue

        match opcao:
            case "x":
                break
            case "a":
                item = input("Item para adicionar: ")
                adicionarItem(listaCompras, item)
            case "b":
                item = input("Item para remover: ")
                removerItem(listaCompras, item)
            case "c":
                exibirItens(listaCompras)
            case "d":
                listaOrdenada = ordenarLista(listaCompras)
                print(listaOrdenada)
            case "e":
                item = input("Item para verificar se existe: ")
                if exists(listaCompras, item):
                    print(f"item {item} existe na lista")
                else:
                    print(f"item {item} NÃO existe na lista")
            case "f":
                salvarLista(listaCompras)
            case "g":
                listaCompras = lerLista()

main()