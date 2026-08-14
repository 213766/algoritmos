nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

avg = (nota1 + nota2 + nota3) / 3

if avg >= 7.0:
    print(f"APROVADO, media {avg}")
else:
    print(f"REPROVADO, media {avg}")