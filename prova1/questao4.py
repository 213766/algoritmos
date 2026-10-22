while True:
    try:
        nrAlunos = int(input("Insira o numero de alunos: "))
        break
    except:
        print("Insira um numero inteiro, válido.")
        continue

totalVeiculos = 0
lugaresVazios = 0

veiculos40 = 0
veiculos15 = 0
veiculos8 = 0
veiculos4 = 0

while nrAlunos >= 40:
    totalVeiculos += 1
    if nrAlunos >= 40:
        nrAlunos -= 40
    else:
        nrAlunos = 0
    veiculos40 += 1

while nrAlunos >= 15:
    totalVeiculos += 1
    if nrAlunos >= 15:
        nrAlunos -= 15
    else:
        nrAlunos = 0
    veiculos15 += 1

while nrAlunos >= 8 or nrAlunos > 4:
    totalVeiculos += 1
    if nrAlunos >= 8:
        nrAlunos -= 8
    else:
        lugaresVazios = 8 - nrAlunos
        nrAlunos = 0
    veiculos8 += 1

while nrAlunos >= 4:
    totalVeiculos += 1
    if nrAlunos >= 4:
        nrAlunos -= 4
    else:
        nrAlunos = 0
    veiculos4 += 1

if nrAlunos > 0:
    totalVeiculos += 1
    lugaresVazios = 4 - nrAlunos
    veiculos4 += 1

print(f"Veículos de  40 lugares: {veiculos40}")
print(f"Veículos de  15 lugares: {veiculos15}")
print(f"Veículos de  8 lugares: {veiculos8}")
print(f"Veículos de  4 lugares: {veiculos4}")
print("\n")
print(f"Total de Veículos: {totalVeiculos}")
print(f"Lugares Vazios: {lugaresVazios}")