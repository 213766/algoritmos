tamanho_sala = {
    'assentos': 10,
    'filas': 8
}

sala = []
for i in range(0, tamanho_sala['filas']):
    cadeiras = []
    for j in range(0, tamanho_sala['assentos']):
        cadeiras.append('O')
    sala.append(cadeiras)

def print_sala():

    a = []

    for b in range(1, tamanho_sala["assentos"] + 1):
        a.append(f"{b:02d}")
    texto = (" | ".join(a)) + " | "
    print("          " + texto)

    a = []
    cont_fila = 1

    for i in sala:
        a.append(f"Fila {cont_fila:02d} | " + " | ".join(str(j).zfill(2).replace("0", " ") for j in i) + " |")
        cont_fila += 1
    print("\n".join(a))

print_sala()