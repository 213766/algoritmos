arquivo = open("./aula10/att2/texto.txt", "r")
texto = ""
for linha in arquivo.readlines():
    texto += linha
# texto = input("Coloque um texto: ")
texto = texto.split(" ")
contagemPalavras = dict()
for palavra in texto:
    contagemPalavras[palavra] = contagemPalavras.get(palavra, 0) + 1

print(contagemPalavras)