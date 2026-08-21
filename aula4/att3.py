import sys

valorA = int(input('insira o primeiro valor: '))
valorB = int(input('insira o segundo valor: '))

if valorB == valorA:
    print(f'valores iguais, são multiplos.')
else:
    if valorA > valorB:
        isMultiplos =  valorA % valorB == 0
    else:
        isMultiplos =  valorB % valorA == 0

    if isMultiplos:
        print(f'São Múltiplos.')
    else:
        print(f'Não são Múltiplos.')