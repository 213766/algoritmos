def isTriangulo(ladoA, ladoB, ladoC):
    return abs(ladoB - ladoC) < ladoA and ladoA < ladoB + ladoC

def tipoTringulo(ladoA, ladoB, ladoC):

    if isTriangulo(ladoA, ladoB, ladoC):
        if ladoA == ladoB and ladoB == ladoC:
            return "EQUILATERO"
        elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            return "ISÓCELES"
        else:
            return "ESCALENO"
    else:
        return "ERRO NÃO TRIANGULO!!!"

print(tipoTringulo(3,4,5))
print(tipoTringulo(3,3,3))
print(tipoTringulo(4,4,5))
print(tipoTringulo(85,72,2))