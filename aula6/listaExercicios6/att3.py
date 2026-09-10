vogais = {'a','e','i','o','u'}
consoantes = []

for _ in range(10):
    l = input('Insira uma letra: ')
    if l.lower() not in vogais:
        consoantes.append(l)
print(f'foram encontradas {len(consoantes)} consoantes')
print(consoantes)