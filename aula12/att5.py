tamanho_sala = {
    'assentos': 10,
    'filas': 8
}

sala = []
for i in range(0, tamanho_sala['filas']):
    cadeiras = []
    for j in range(0, tamanho_sala['assentos']):
        cadeiras.append('O')
    sala.append(cadeiras)

def print_sala():

    a = []

    for b in range(1, tamanho_sala["assentos"] + 1):
        a.append(f"{b:02d}")
    texto = (" | ".join(a)) + " | "
    print("          " + texto)

    a = []
    cont_fila = 1

    for i in sala:
        a.append(f"Fila {cont_fila:02d} | " + " | ".join(str(j).zfill(2).replace("0", " ") for j in i) + " |")
        cont_fila += 1
    print("\n".join(a))

# Menu de selcao
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

def menuSelecao() -> int:
    opcoes = {
        1: 'Exibir mapa de assentos ',
        2: 'Reservar assento',
        3: 'Cancelar reserva',
        4: 'Consultar ocupação',
        5: 'Verificar fileira',
        6: 'Encerrar'
    }

    print("Menu opção:")
    for opcao, descricao in opcoes.items():
        print(f'{opcao} - {descricao}')
    opcao = getSelecaoValida('Selecione uma opcao: ', opcoes.keys())
    return opcao

def main():
    while True:
        selecao = menuSelecao()
        if selecao == 1:
            print_sala()
        elif selecao == 2:
            while True:
                fila = getSelecaoValida("Insira a fila a reservar: ", range(1, tamanho_sala["filas"] + 1)) - 1
                coluna = getSelecaoValida("Insira o assento a reservar: ", range(1, tamanho_sala["assentos"] + 1)) - 1
                if sala[fila][coluna].strip() == "X":
                    print("Assento Reservado, esolha outro.")
                else:
                    sala[fila][coluna] = sala[fila][coluna].replace("O", "X")
                    break
        elif selecao == 3:
            while True:
                fila = getSelecaoValida("Insira a fila a cancelar: ", range(1, tamanho_sala["filas"] + 1)) - 1
                coluna = getSelecaoValida("Insira o assento a cancelar: ", range(1, tamanho_sala["assentos"] + 1)) - 1
                if sala[fila][coluna].strip() == "O":
                    print("Assento NÃO Reservado, esolha outro.")
                else:
                    sala[fila][coluna] = sala[fila][coluna].replace("X", "O")
                    break
        elif selecao == 4:
            nrAssentos = tamanho_sala["filas"] * tamanho_sala["assentos"]
            nrOcupados = 0
            for i in range(0, tamanho_sala['filas']):
                for j in range(0, tamanho_sala['assentos']):
                    if sala[i][j].strip() == "X":
                        nrOcupados += 1
            print(f"Ocupados: {nrOcupados}, {round(nrOcupados/nrAssentos,2)*100:.0f}%")
        elif selecao == 5:
            nrOcupados = 0
            fila = sala[getSelecaoValida("Selecione a fila a validar: ", range(1, tamanho_sala["filas"] + 1)) - 1]
            for j in fila:
                if j.strip() == "X":
                    nrOcupados += 1
            print(f"Ocupados: {nrOcupados}, {round(nrOcupados/tamanho_sala["assentos"],2)*100:.0f}%")
        elif selecao == 6:
            break

main()