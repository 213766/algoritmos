def isPalindromo(palavra:str):
    separado = list(palavra)
    copia = separado.copy()
    separado.reverse()
    return separado == copia

print(isPalindromo('abcba'))