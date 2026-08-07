def ajustarNota (nota: float, peso: float):
    return nota * peso

notaProvaA = float(input("Insira a nota da prova A: "))
notaProvaB = float(input("Insira a nota da prova B: "))
notaTrabalhos = float(input("Insira a nota da prova C: "))

notaProvaAPond = ajustarNota(notaProvaA, 3)
notaProvaBPond = ajustarNota(notaProvaB, 5)
notaTrabalhosPond = ajustarNota(notaTrabalhos, 2)

media = (notaProvaAPond + notaProvaBPond + notaTrabalhosPond) / 10

print(media)