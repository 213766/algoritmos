SENHA = '2023'
count = 0

while True:
    senhaInpt = input('Insira sua senha: ')

    if senhaInpt == SENHA:
        print('ACESSO PERMITIDO')
        print(f'foram realizadas {count} tentativas')
        break
    else:
        print('SENHA INVÁLIDA')
        count += 1