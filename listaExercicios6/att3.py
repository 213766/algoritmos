vogais = ('a','e','i','o','u')
consoantes = 0

for _ in range(10):
    l = input('Insira uma letra: ')
    if l.lower() not in vogais:
        consoantes += 1
print(f'foram encontradas {consoantes} consoantes')