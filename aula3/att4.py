notas = []

for _ in range(3):
    notas.append(int(input("Insira um Número: ")))

notas.sort()

print(f"menor: {notas[0]}; intermediario: {notas[1]}; maior: {notas[2]}")