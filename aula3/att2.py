num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

while num1 == num2:
    num2 = int(input(f'Números iguais, insira um número diferente de {num1}: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num2} é maior que {num1}')