num1 = int(input('insira um numero inteiro menor: '))

while True:

    num2 = int(input('insira um numero inteiro maior: '))

    if num2 <= num1:
        print(f'Insira um numero maior que {num1}')
    else:
        break

pares = []
impares = []

for i in range(num1 + 1,num2):

    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Os numeros pares entre {num1} e {num2} são:')
print(pares)
print(f'Os numeros impares entre {num1} e {num2} são:')
print(impares)