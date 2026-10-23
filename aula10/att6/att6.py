from os import path
import json

campos = {
    'nome': '',
    'quantidadeEstoque': '',
    'preco': ''
}
try:
    with open(f"{path.dirname(path.abspath(__file__))}/crud.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
except:
    dados = {}

print("Selecione uma opção:")
while True:
    try:
        opcao = int(input("1 - Inserir\n2 - Alterar\n3 - Remover\n4-Ler\n5-Salvar JSON\n-1 - Encerrar programa\n"))
        if opcao not in (-1, 1, 2, 3, 4,5):
            print("Selecione um número válido!")
            continue
    except:
        print("Insira um número!")
        continue
    
    if opcao == 1:
        cod = input('Insira o codigo do produto: ')
        produto = campos.copy()
        for campo in campos.keys():
            produto[campo] = input(f'Insira o(a) {campo} do produto: ')

        dados[cod] = produto

    if opcao == 2:
        opp = []
        for i in dados.keys():
            print(i, dados[i])
            opp.append(i)

        while True:
            produto = input("Insira o ID de um usuário para alterar: ")
            if produto in opp: 
                produto = dados[produto]
                break
            else:
                print('Selecione opcao valida.')

        while True:
            print('selecione campo para alterar:')
            contI = 1
            for i in campos.keys():
                print(f'{contI}-{i}')
                contI += 1
            print('-1-Cancela')
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
            if idCampo == 2: campo = 'quantidadeEstoque'
            if idCampo == 3: campo = 'preco'
            if idCampo == -1: break

            produto[campo] = input(f'Insira o novo valor para {campo}: ')



    if opcao == 3:
        opp = []
        for i in dados.keys():
            print(i, dados[i])
            opp.append(i)

        while True:
            produto = input("Insira o ID de um usuário para deletar: ")
            if produto in opp: 
                dados.pop(produto)
                break
            else:
                print('Selecione opcao valida.')

    if opcao == 4:
        for us in dados.values():
            print(us)

    if opcao == 5:
        with open(f"{path.dirname(path.abspath(__file__))}/crud.json", "w", encoding="utf-8") as f:
            json.dump(dados,f, ensure_ascii=False,indent=4)

    if opcao == -1:
        break