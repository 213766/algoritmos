pos = 0
neg = 0

for _ in range(9):
    num = int(input("Insira um numero inteiro: "))
    
    if num >= 0:
        pos += 1
    else:
        neg += 1

print(f'foram {pos} numero(s) positivo(s) e {neg} negativo(s)')