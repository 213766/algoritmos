import random

def getSelecaoValida(mensagem, opcoes) -> int:
    while True:
        try:
            selecionado = int(input(mensagem).strip())
            if selecionado not in opcoes:
                print("Selecione um número válido!")
                continue
            break
        except:
            print("Insira um número!")
            continue
    return selecionado

topNumero = 100
numero = random.randint(1, topNumero)

maxChances = 10
tentativas = 0

print(f"Tente adivinhar o número entre 1 e {topNumero}")
while True:
    if tentativas >= maxChances:
        print("é, não foi dessa vez...\nTente novamente.")
        break
    print(f"você tem {maxChances - tentativas} chance(s):")
    chute = getSelecaoValida("Qual seu chute?", range(1, topNumero + 1))
    if chute == numero:
        print("Parabéns! Você acertou!")
        break
    print(f"O número é {"maior" if numero > chute else "menor"} que {chute}.")
    tentativas += 1