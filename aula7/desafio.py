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

# for produto in produtos:
#     if produto[1] > melhorProduto[1]:
#         melhorProduto = produto

print(faturamentoTotal)
print(produtos.keys())
print(produtos)