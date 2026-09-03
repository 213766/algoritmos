soma = 0
nrNumeros = 0

while soma <= 100:

    if soma == 0:
        num = int(input('Insira um numero: '))
    else:
        num = int(input(f'Sua soma ({soma}), ainda é menor que 100, insira outro numero: '))

    if num != 0:
        soma += num
        nrNumeros += 1

print(f'Sua soma deu {soma}, foram necessários {nrNumeros}')