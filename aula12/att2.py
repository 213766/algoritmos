import random

palavras = ["universidade", "faculdade", "atividade", "forca"]

palavra = palavras[random.randint(0, len(palavras)) - 1].upper()
forca = "_" * len(palavra)
maxErros = 3
erros = 0

print(forca)

while True:

    while True:
        chute = input("Selecione uma letra ou chute a palavra:\n").strip().upper()
        if not chute.isalpha():
            print("Selecione uma letra válida!")
            continue
        break

    if chute == palavra:
        forca = chute
        print("Parabéns! Você acertou!")
        break
    if chute in palavra:
        for indexLetra in range(0, len(palavra)):
            letra = palavra[indexLetra]
            if letra == chute:
                forca = forca[ : indexLetra] + chute + forca[indexLetra + 1 :]
        print(forca)
    else:
        erros += 1
        print(f"Errou. Você tem {maxErros - erros} tentativas")

    if erros == maxErros:
        print("Você perdeu...")
        break

    if "_" not in forca:
        print(f"Parabéns! Você acertou.\nA palavra era {forca}")
        break