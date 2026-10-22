texto = input("Coloque um texto: ")
texto.replace(" ", "")
contagemLetras = dict()
for letra in texto:
    contagemLetras[letra] = contagemLetras.get(letra, 0) + 1

print(contagemLetras)