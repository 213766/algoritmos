ORDINAL = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto')

def coletarNotas():
    notas = []
    for i in range(5):
        nota = float(input(f'insira a distancia do {ORDINAL[i]} salto : '))
        notas.append(nota)
    return notas

nome: str

nome = input('Insira o nome do Atleta: ')

if nome.strip() == "":
    print('Encerrando...')
else:
    notas = coletarNotas()
    strNotas = []

    print(f'\nAtleta: {nome}')
    for i in range(5):
        t = ORDINAL[i] + ' salto: '
        t = t.title()
        nota = round(notas[i],1)
        print(t + str(nota) + ' m')
        strNotas.append(str(notas[i]))
    strNotas = ' - '.join(strNotas)
    media = round(sum(notas) / len(notas),1)
    print(f'\nResultado final:\nAtleta: {nome}\nSaltos: {strNotas}\nMédia dos saltos: {media} m')