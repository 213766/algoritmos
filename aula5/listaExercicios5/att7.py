for _ in range(9):
    while True:
        num = int(input("Insira um numero inteiro: "))

        if num != 0:
            if num > 0:
                print('Positivo')
            else:
                print('Negativo')
            break
        else:
            print('Selecione um numero diferente de 0')