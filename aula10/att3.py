def exists(lista, item):
    return item in lista

def salvarLista(lista):
    arquivo = open("./prova1/lista_alunos.txt", "w")
    arquivo.write("\n".join(lista))

palavras = {}

print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir Palavra\n2 - Alterar Palavra\n3 - Remover Palavra\n4 - Traduzir\n5 - Exibir Palavras\n6 - Encerrar programa\n"))
        if opcao not in (1,2,3,4,5,6):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        palavra = input("Insira a palavra para adicionar: ")
        traducao = input("Insira a tradução da palavra para adicionar: ")
        if exists(palavras, palavra):
            print("ERROR: Palavra já existe.")
        else:
            palavras[palavra] = traducao
    if opcao == 2:
        palavra = input("Insira a palavra para alterar a tradução: ")
        if exists(palavras, palavra):
            traducao = input("Insira a nova tradução: ")
            palavras[palavra] = traducao
        else:
            print("ERROR: palavra NÃO existe")
    if opcao == 3:
        palavra = input("Insira a palavra para remover: ")
        if exists(palavras, palavra):
            palavras.pop(palavra)
        else:
            print("ERROR: palavra NÃO existe")
    if opcao == 4:
        palavra = input("Insira a palavra para traduzir: ")
        if len(palavras) > 0:
            print(palavras[palavra])
                
        else:
            print("Sem palavras para apresentar")
    if opcao == 5:
        for palavra, traducao in palavras.items():
            print(f"{palavra}: {traducao}")
    if opcao == 6:
        break