produtos = {
    101: {"nome": "Teclado", "preco": 120.00, "estoque": 10},
    102: {"nome": "Mouse", "preco": 65.00, "estoque": 15},
    103: {"nome": "Monitor", "preco": 850.00, "estoque": 5},
    104: {"nome": "Webcam", "preco": 180.00, "estoque": 8},
    105: {"nome": "Headset", "preco": 145.00, "estoque": 12},
    106: {"nome": "Pendrive 64GB", "preco": 45.00, "estoque": 30},
    107: {"nome": "SSD 480GB", "preco": 280.00, "estoque": 7},
    108: {"nome": "HD Externo 1TB", "preco": 350.00, "estoque": 6},
    109: {"nome": "Memória RAM 8GB", "preco": 160.00, "estoque": 14},
    110: {"nome": "Placa de Vídeo", "preco": 1850.00, "estoque": 3},
    111: {"nome": "Processador", "preco": 950.00, "estoque": 4},
    112: {"nome": "Placa-mãe", "preco": 680.00, "estoque": 5},
    113: {"nome": "Fonte 600W", "preco": 320.00, "estoque": 9},
    114: {"nome": "Gabinete", "preco": 250.00, "estoque": 6},
    115: {"nome": "Caixa de Som", "preco": 95.00, "estoque": 11}
}

# A)
idProduto = 102
print(f'nome do produto {idProduto}: {produtos[idProduto]['nome']}')

# B)
nomeTrocarPreco = 'teclado'
novoPreco = 135.00
for idProduto, produto in produtos.items():
    if produto['nome'].lower() == nomeTrocarPreco.lower():
        print(f'preco antigo: {produtos[idProduto]['preco']}')
        produtos[idProduto]['preco'] = novoPreco
        print(f'preco novo: {produtos[idProduto]['preco']}')

# C)
novoProduto = {
    'nome': 'Webcam',
    'preco': 180.00,
    'estoque': 8
}
idNovoProduto = 104
produtos[idNovoProduto] = novoProduto
print(f'novo produto: {produtos[idNovoProduto]}')

# D)
idProduto = 103
produtos.pop(idProduto)
try:
    print(produtos[idProduto])
except:
    print(f'Produto {idProduto} removido.')

# E)
for produto in produtos.values():
    print(produto)

# F)
valorEstoque = 0
for produto in produtos.values():
    valorEstoque += produto['estoque'] * produto['preco']
print(f'Valor Total Estoque: {valorEstoque}')