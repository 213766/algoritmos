def pegarValor(lado):
    while True:
        medLado = int(input(f"Insira a medida do lado {lado}: "))
        if medLado > 0:
            break
    return medLado


ladoA = pegarValor("A")
ladoB = pegarValor("B")
ladoC = pegarValor("C")

isTriangulo = abs(ladoB - ladoC) < ladoA and ladoA < ladoB + ladoC

if isTriangulo:
    if ladoA == ladoB and ladoB == ladoC:
        print("Triangulo EQUILATERO")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triangulo ISÓCELES")
    else:
        print("Triangulo ESCALENO")
else:
    print("ERRO NÃO TRIANGULO!!!")