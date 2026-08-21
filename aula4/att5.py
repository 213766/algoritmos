def getPessoa(idPessoa):
    nome = input(f'insira o nome da pessoa {idPessoa}: ')
    idade = input(f'insira a idade da pessoa {idPessoa}: ')
    return [nome, idade]

pessoa1 = getPessoa(1)
pessoa2 = getPessoa(2)
pessoa3 = getPessoa(3)

if pessoa1[1] > pessoa2[1] and pessoa1[1] > pessoa3[1]:
    maisVelho = pessoa1
elif pessoa2[1] > pessoa1[1] and pessoa2[1] > pessoa3[1]:
    maisVelho = pessoa2
elif pessoa3[1] > pessoa1[1] and pessoa3[1] > pessoa2[1]:
    maisVelho = pessoa3

if pessoa1[1] < pessoa2[1] and pessoa1[1] < pessoa3[1]:
    maisNovo = pessoa1
elif pessoa2[1] < pessoa1[1] and pessoa2[1] < pessoa3[1]:
    maisNovo = pessoa2
elif pessoa3[1] < pessoa1[1] and pessoa3[1] < pessoa2[1]:
    maisNovo = pessoa3

print(f'O(a) {maisVelho[0]} é o mais velho e o {maisNovo[0]} é o mais novo')