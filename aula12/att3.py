tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
opcoes = [1,2,3,4,5,6,7,8,9]

def print_tabuleiro():
    tab = []
    for i in tabuleiro:
        tab.append(" " + " | ".join(str(j) for j in i) + " ")
    print("\n---|---|---\n".join(tab))

def getSelecaoValida(mensagem, opcoes) -> int:
    while True:
        try:
            selecionado = int(input(mensagem).strip())
            if selecionado not in opcoes:
                print("Selecione um número válido!")
                continue
            break
        except:
            print("Insira um número!")
            continue
    return selecionado

def temVencedor()->bool:
    if (
        tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] or
        tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] or
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] or

        tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] or
        tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] or
        tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] or

        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]
    ):
        return True

jogador = "O"
jogadas = 0

while True:

    print_tabuleiro()
    posicao = getSelecaoValida(f"jogador '{jogador}' selecione a posicao: ", opcoes)
    opcoes.remove(posicao)
    col = (posicao - 1) // 3
    lin = (posicao - col * 3) - 1
    tabuleiro[col][lin] = jogador

    if temVencedor():
        print_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break
    jogador = ("X" if jogador == "O" else "O")

    jogadas += 1

    if jogadas == 9:
        print("Empate")
        break