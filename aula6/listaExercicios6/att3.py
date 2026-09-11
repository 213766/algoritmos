vogais = ('a','e','i','o','u')
listConsoantes = []

for _ in range(10):
    l = input('Insira uma letra: ')
    if l.lower() not in vogais and l.lower().isalpha():
        listConsoantes.append(l)
print(f'foram encontradas {len(listConsoantes)} listConsoantes')
print(listConsoantes)