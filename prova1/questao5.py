def exists(lista, item):
    copia = lista.copy()
    try:
        copia.remove(item)
        return True
    except:
        return False

def salvarLista(lista):
    arquivo = open("./prova1/lista_alunos.txt", "w")
    arquivo.write("\n".join(lista))

alunos = []

print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir aluno\n2 - Alterar aluno\n3 - Remover aluno\n4 - Listar alunos\n5 - Exportar alunos\n6 - Encerrar programa\n"))
        if opcao not in (1,2,3,4,5,6):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        nomeAluno = input("Insira o nome do aluno para adicionar: ")
        if exists(alunos, nomeAluno):
            print("ERROR: Aluno já existe.")
        else:
            alunos.append(nomeAluno)
    if opcao == 2:
        nomeAluno = input("Insira o nome do aluno para alterar: ")
        if exists(alunos, nomeAluno):
            alunos.remove(nomeAluno)
            nomeAluno = input("Insira o nome novo do aluno: ")
            alunos.append(nomeAluno)
        else:
            print("ERROR: Aluno NÃO existe")
    if opcao == 3:
        nomeAluno = input("Insira o nome do aluno para remover: ")
        if exists(alunos, nomeAluno):
            alunos.remove(nomeAluno)
        else:
            print("ERROR: Aluno NÃO existe")
    if opcao == 4:
        if len(alunos) > 0:
            alunos.sort()
            i = 1
            for aluno in alunos:
                print(f"{i}. {aluno}")
                i += 1
                
        else:
            print("Sem alunos para apresentar")
    if opcao == 5:
        salvarLista(alunos)
    if opcao == 6:
        break