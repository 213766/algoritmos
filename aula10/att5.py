import random

misterios = {
    1: {'misterio': 'Uma linguagem de programação poderosa.', 'resposta': 'python'},
    2: {'misterio': 'quem fez esse codigo.', 'resposta': 'gustavo'},
}

tentativasMax = 3
tentativas = 0
resultado = False

rand = random.randint(1 ,len(misterios))
misterio = misterios[rand]

while not resultado and tentativas < tentativasMax:
    resp = input(f'{misterio['misterio']}:').lower
    resultado = resp == misterio['resposta']
    tentativas += 1

if resultado:
    print('PARABENS!! VC ACERTOU')
else:
    print(f'TCH TCH TCH, tao facil e perdeu... a resposta era {misterio['resposta']}.')