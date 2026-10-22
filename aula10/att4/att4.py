from os import path
import json

def exists(lista, item):
    return item in lista

def salvarLista(lista):
    arquivo = open("./prova1/lista_alunos.txt", "w")
    arquivo.write("\n".join(lista))

usuarios = {}
camposUsuario = {
    'nome': '',
    'email': '',
    'idade': ''
}
id = 0
try:
    with open(f"{path.dirname(path.abspath(__file__))}/crud.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
except:
    dados = {}

for idd in dados.keys():
    if idd > id: id = idd

print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir\n2 - Alterar\n3 - Remover\n4-Ler todos usuarios\n5-Salvar JSON\n-1 - Encerrar programa\n"))
        if opcao not in (-1, 1, 2, 3, 4,5):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        usuario = camposUsuario.copy()
        for campo in camposUsuario.keys():
            usuario[campo] = input(f'Insira o(a) {campo} do usuario: ')

        dados[id] = usuario

        id += 1

    if opcao == 2:
        opp = []
        for i in dados.keys():
            print(i, dados[i])
            opp.append(i)

        while True:
            try:
                usuario = int(input("Insira o ID de um usuário para alterar: "))
                if usuario in opp: 
                    usuario = dados[usuario]
                    break
                else:
                    print('Selecione opcao valida.')
            except:
                print('Insira um ID!!!')

        while True:
            print('selecione campo para alterar:\n1-nome\n2-email\n3-idade\n-1-Cancela')
            while True:
                try:
                    idCampo = int(input("Insira a opcao do campo: "))
                    if idCampo in (1,2,3,-1):
                        break
                    else:
                        print('Selecione opcao valida.')
                except:
                    print('Insira um ID!!!')

            if idCampo == 1: campo = 'nome'
            if idCampo == 2: campo = 'email'
            if idCampo == 3: campo = 'idade'
            if idCampo == -1: break

            usuario[campo] = input(f'Insira o novo valor para {campo}: ')



    if opcao == 3:
        opp = []
        for i in dados.keys():
            print(i, dados[i])
            opp.append(i)

        while True:
            try:
                usuario = int(input("Insira o ID de um usuário para deletar: "))
                if usuario in opp: 
                    dados.pop(usuario)
                    break
                else:
                    print('Selecione opcao valida.')
            except:
                print('Insira um ID!!!')

    if opcao == 4:
        for us in dados.values():
            print(us)

    if opcao == 5:
        with open(f"{path.dirname(path.abspath(__file__))}/crud.json", "w", encoding="utf-8") as f:
            json.dump(dados,f, ensure_ascii=False,indent=4)

    if opcao == -1:
        break