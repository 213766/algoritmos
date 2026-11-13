def getSelecaoValida(mensagem, opcoes=[]) -> int:
    while True:
        try:
            selecionado = int(input(mensagem).strip())
            if opcoes:
                if selecionado not in opcoes:
                    print("Selecione um número válido!")
                    continue
            break
        except:
            print("Insira um número!")
            continue
    return selecionado

def menuSelecao() -> int:
    opcoes = {
        1: 'traduzir',
        2: 'criptografar',
        -1: 'Encerrar programa'
    }

    print("Menu opção:")
    for opcao, descricao in opcoes.items():
        print(f'{opcao} - {descricao}')
    opcao = getSelecaoValida('Selecione uma opcao: ', opcoes.keys())
    return opcao

def traduzir(chave, mensagem):
    mensagemNova = []
    for letra in mensagem:
        mensagemNova.append(chr(ord(letra) - chave))
    mensagemNova = "".join(str(x) for x in mensagemNova)
    return mensagemNova

def criptografar(chave, mensagem):
    mensagemNova = []
    for letra in mensagem:
        mensagemNova.append(chr(ord(letra) + chave))
    mensagemNova = "".join(str(x) for x in mensagemNova)
    return mensagemNova

chave = getSelecaoValida("deslocamento: ")

while True:
    match menuSelecao():
        case 1:
            mensagem = input("Insira sua frase: ")
            print(traduzir(chave, mensagem))
        case 2:
            mensagem = input("Insira sua frase: ")
            print(criptografar(chave, mensagem))
        case -1:
            break