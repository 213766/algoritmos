from os import path

def exists(lista, item):
    return item in lista

def salvarLista(lista):
    arquivo = open("./prova1/lista_alunos.txt", "w")
    arquivo.write("\n".join(lista))

usuarios = {}
file = open(f"{path.dirname(path.abspath(__file__))}/crud.txt", "w", encoding="utf-8")


print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir\n2 - Alterar\n3 - Remover\n4 - Ler\n-1 - Encerrar programa\n"))
        if opcao not in (-1, 1, 2, 3, 4):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        usuario = input("Insira o usuario para adicionar: ").lower().title()
        
        if exists(usuarios, usuario):
            print("ERROR: usuario já existe.")
        else:
            usuarios[usuario] = traducao
    if opcao == 2:
        usuario = input("Insira a usuario para alterar a tradução: ").lower()
        if exists(usuarios, usuario):
            traducao = input("Insira a nova tradução: ").lower()
            usuarios[usuario] = traducao
        else:
            print("ERROR: usuario NÃO existe")
    if opcao == 3:
        usuario = input("Insira a usuario para remover: ").lower()
        if exists(usuarios, usuario):
            usuarios.pop(usuario)
        else:
            print("ERROR: usuario NÃO existe")
    if opcao == 4:
        usuario = input("Insira a usuario para traduzir: ").lower()
        if len(usuarios) > 0:
            print(usuarios[usuario])    
        else:
            print("Sem usuarios para apresentar")
    if opcao == -1:
        break