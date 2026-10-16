from os import path

def exists(lista, item):
    return item in lista

def salvarLista(lista):
    arquivo = open("./prova1/lista_alunos.txt", "w")
    arquivo.write("\n".join(lista))

palavras = {}

print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir Palavra\n2 - Alterar Palavra\n3 - Remover Palavra\n4 - Traduzir\n5 - Exibir Palavras\n6 - Salvar Arquivo\n7 - Carregar Arquivo\n8 - Traduzir arquivo\n-1 - Encerrar programa\n"))
        if opcao not in (-1, 1, 2, 3, 4, 5, 6, 7, 8):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        palavra = input("Insira a palavra para adicionar: ").lower()
        traducao = input("Insira a tradução da palavra para adicionar: ").lower()
        if exists(palavras, palavra):
            print("ERROR: Palavra já existe.")
        else:
            palavras[palavra] = traducao
    if opcao == 2:
        palavra = input("Insira a palavra para alterar a tradução: ").lower()
        if exists(palavras, palavra):
            traducao = input("Insira a nova tradução: ").lower()
            palavras[palavra] = traducao
        else:
            print("ERROR: palavra NÃO existe")
    if opcao == 3:
        palavra = input("Insira a palavra para remover: ").lower()
        if exists(palavras, palavra):
            palavras.pop(palavra)
        else:
            print("ERROR: palavra NÃO existe")
    if opcao == 4:
        palavra = input("Insira a palavra para traduzir: ").lower()
        if len(palavras) > 0:
            print(palavras[palavra])    
        else:
            print("Sem palavras para apresentar")
    if opcao == 5:
        for palavra, traducao in palavras.items():
            print(f"{palavra}: {traducao}")
    if opcao == 6:
        file = open(f"{path.dirname(path.abspath(__file__))}/file.txt", "w", encoding="utf-8")
        for chave, valor in palavras.items():
            file.write(f"{chave}:{valor}\n")
        file.close()
    if opcao == 7:
        file = open(f"{path.dirname(path.abspath(__file__))}/file.txt", "r", encoding="utf-8")
        for lin in file.readlines():
            lin = lin.replace("\n","")
            dict = lin.split(":")
            print(dict)
            try:
                if dict[0] != "": palavras[dict[0]] = dict[1]
            except:
                continue
    if opcao == 8:
        file = open(f"{path.dirname(path.abspath(__file__))}/Texto.txt", "r", encoding="utf-8")
        fileTraduzido = open(f"{path.dirname(path.abspath(__file__))}/fileTraduzido.txt", "w", encoding="utf-8")
        for lin in file.readlines():
            for palavraTxt in lin.split():
                palavra = palavraTxt.lower()
                if palavra in palavras.keys():
                    lin = lin.replace(f"{palavraTxt}", f"{palavras[palavra]}", 1)
            fileTraduzido.write(lin)
        fileTraduzido.close()
        file.close()
    if opcao == -1:
        break