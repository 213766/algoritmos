cardapio = {
    1: {"nome": "Hambúrguer", "preco": 25.00},
    2: {"nome": "Batata frita", "preco": 12.00},
    3: {"nome": "Suco", "preco": 8.00},
    4: {"nome": "Refrigerante", "preco": 7.00},
    5: {"nome": "Cheeseburger", "preco": 28.00},
    6: {"nome": "X-Bacon", "preco": 32.00},
    7: {"nome": "X-Salada", "preco": 27.00},
    8: {"nome": "Pizza individual", "preco": 30.00},
    9: {"nome": "Cachorro-quente", "preco": 18.00},
    10: {"nome": "Pastel", "preco": 10.00},
    11: {"nome": "Água mineral", "preco": 4.00},
    12: {"nome": "Milk-shake", "preco": 16.00},
    13: {"nome": "Sorvete", "preco": 9.00},
    14: {"nome": "Café", "preco": 5.00},
    15: {"nome": "Brownie", "preco": 11.00}
}

pedidos = {
    1: {1: 2, 2: 3, 3: 2},
    2: {5: 2, 4: 2, 13: 1},
    3: {6: 1, 2: 2, 11: 2},
    4: {8: 2, 3: 3},
    5: {9: 3, 10: 2, 4: 3},
    6: {7: 2, 12: 2, 14: 2},
    7: {1: 1, 5: 1, 2: 2},
    8: {10: 4, 11: 3},
    9: {6: 2, 3: 2, 15: 2},
    10: {8: 1, 13: 3, 14: 2},
    11: {9: 2, 4: 2, 12: 1},
    12: {5: 3, 2: 3, 3: 3},
    13: {7: 1, 1: 2, 15: 1},
    14: {6: 1, 8: 1, 11: 4},
    15: {12: 3, 13: 2, 10: 2}
}

# A)
def consultarCardapio():
    for id, item in cardapio.items():
        print(f'{id} - {item['nome']}: R${item['preco']}')

# B e F)
def consultarPedidoMesa(codigoMesa:int):
    pedido = pedidos[codigoMesa]
    totalMesa = 0
    print(f'Pedido Mesa {codigoMesa}:')
    for codigoItem, quantidade in pedido.items():
        print(f'{quantidade} x {cardapio[codigoItem]['nome']}({codigoItem}) | R${quantidade * cardapio[codigoItem]['preco']}')
        totalMesa += quantidade * cardapio[codigoItem]['preco']
    print(f'Total Mesa: R${totalMesa}')

# C e D)
def adicionarModificarPedido(codigoPedido, codigoProduto, quantidade):
    pedido = pedidos[codigoPedido]
    pedido[codigoProduto] = quantidade
    pedidos[codigoPedido] = pedido

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
        1: 'Consultar cardápio',
        2: 'Consultar pedido da mesa',
        3: 'Realizar pedido',
        4: 'Alterar quantidade de um item',
        5: 'Remover item do pedid',
        6: 'Calcular a conta da mesa',
        7: 'Listar mesas com pedidos',
        -1: 'Encerrar programa'
    }

    print("Menu opção:")
    for opcao, descricao in opcoes.items():
        print(f'{opcao} - {descricao}')
    opcao = getSelecaoValida('Selecione uma opcao: ', opcoes.keys())
    return opcao

def main():
    while True:
        opcao = menuSelecao()

        if opcao == 1:
            consultarCardapio()
            
        if opcao in (2, 6):
            mesa = getSelecaoValida('Selecione uma mesa: ', pedidos.keys())
            consultarPedidoMesa(mesa)
            
        if opcao in (3, 4):
            mesa = getSelecaoValida('Seleciona uma mesa: ', pedidos.keys())
            codigoPedido = getSelecaoValida('Selecione um item do cardapio: ', cardapio.keys())
            quantidade = int(input('Selecione a quantidade: '))
            adicionarModificarPedido(mesa, codigoPedido, quantidade)

        if opcao == 5:
            mesa = getSelecaoValida('Seleciona uma mesa: ', pedidos.keys())
            consultarPedidoMesa(mesa)
            pedidoMesa = pedidos[mesa]
            codigoRemover = getSelecaoValida('Selecione um item do pedido: ', pedidoMesa.keys())
            pedidoMesa.pop(codigoRemover)
            
        if opcao == 7:
            print(f'mesas com pedidos: {', '.join(str(pedido) for pedido in pedidos.keys())}')

        if opcao == -1:
            break

main()