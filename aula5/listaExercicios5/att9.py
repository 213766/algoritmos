mediaMinima = float(input('Insira a media minima desejada:'))

sum = 0
count = 0

while True:
    sum += float(input('Insira um Numero: '))
    count += 1

    if sum/count >= mediaMinima:
        print(f'meida minima de {mediaMinima} atingida. Foram necessários {count} numeros. Media final de {sum/count}.')
