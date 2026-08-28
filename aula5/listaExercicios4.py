string = input("coloque sua string: ")

# 1
contagem = len(string)
print(f"numero de caracteres: {contagem}")

# 2
primCaract = string[0]
ultCaract = string[contagem - 1]
print(f"primeiro caractere: {primCaract}, ultimo caractere: {ultCaract}")

# 3 e 4
while True:
    posicao = int(input("Selecione a posicao desejada: "))

    if posicao <= 0 or posicao > 26:
        print(f"selecione uma posicao valido (de 1 a {contagem})")
    else:
        break

caractPosInicio = string[posicao - 1]
caractPosFim = string[-posicao]

print(f"caractere na posicao {posicao} a partir do inicio da string: {caractPosInicio}")
print(f"caractere na posicao {posicao} a partir do fim da string: {caractPosFim}")

# 5 e 6
print(f"string em maiusculo: {string.upper()}")
print(f"string em minusculo: {string.lower()}")

# 7
caractReplace = input("Caractere para ser trocado: ")
caractReplacePor = input("Caractere que sera trocado por: ")
print(f"string com carcateres subtituidos: {string.replace(caractReplace,caractReplacePor)}")

# 8
frase = "A ligeira raposa marrom ataca o cão preguiçoso"

palavras = frase.split(" ")
print(f"na frase {frase} tem {len(palavras)} palavras")

# 9
stringVerificar = input("String a verificar se esta na referencia: ")

if stringVerificar in string:
    print("esta")
else:
    print("nao esta!")

# 10
stringConcatenar = input("string para adicionar ao inicio e ao fim da referencia: ")
print(f"string concatenada: {stringConcatenar + string + stringConcatenar}")

# 11
stringVerificar = input("String a contar repeticoes na referencia: ")
print(f"a string {stringVerificar} aparece {string.count(stringVerificar)} vezes na string")

# 12
stringVerificar = input("String a verificar a posicao na referencia: ")
print(f"posicao da string procurada: {string.find(stringVerificar)}")

# 13 certo agora
if string.isalpha():
    print("tem so letras, certo")
else:
    print("nao tem so letras, certo")

# 14
if string.isnumeric():
    print("tem so numeros")
else:
    print("nao tem so numeros")

# 15
print(string.title())