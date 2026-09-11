vendas = [
    ["Notebook", 2, 3500],
    ["Mouse", 10, 50],
    ["Teclado", 5, 150],
    ["Monitor", 3, 1200],
    ["Mouse", 7, 45],
    ["Notebook", 1, 3400]
]

produtos = {}
faturamentoTotal = 0

for venda in vendas:
    produto = venda[0]
    quantidade = venda[1]
    preco = venda[2]
    valor = quantidade * preco

    faturamentoTotal += (valor)

    if produto not in produtos:
        produtos.update({produto: valor})
    else:
        produtos[produto] += valor

melhorProduto = ["", 0]

for produto, valor in produtos.items():
    if valor > melhorProduto[1]:
        melhorProduto[0] = produto
        melhorProduto[1] = valor

print(f"Faturamento total: {faturamentoTotal}")
print(f"Itens individuais:\n{produtos.keys()}")
print(f"vendas por produto:\n{produtos}")
print(f"Produto com maior faturamento: {melhorProduto}")
