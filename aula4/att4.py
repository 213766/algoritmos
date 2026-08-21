def isDataValida(dia, mes):
    valido = mes > 0 and mes <= 12
    if valido:

        valido = mes in (4,6,9,11) and dia >= 1 and dia <= 30 \
            or mes in (1,3,5,7,8,12) and dia >= 1 and dia <= 31 \
            or mes == 2 and dia >= 1 and dia <= 29

    return valido

nome = input('Insura seu nome: ')

while True:
    data = input("Insira uma Data(dd/mm): ")

    dataSeparada = data.split('/')

    dia = int(dataSeparada[0])
    mes = int(dataSeparada[1])

    if isDataValida(dia, mes):
        break

# transformar data em numero para comparacoes
# inverter data para ano mes dia
# nesse caso será invertido para mes dia

# aqui ele é um valor numerico que pode ser comparado
mesDia = (mes*100)+dia

if dia >= 21 and mes == 1 or dia <= 18 and mes == 2:
    sig = 'aquario'
elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
    sig = 'peixes'
elif dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    sig = 'aries'
elif dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
    sig = 'touro'
elif dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
    sig = 'gemeos'
elif dia >= 22 and mes == 6 or dia <= 22 and mes == 7:
    sig = 'cancer'
elif dia >= 23 and mes == 7 or dia <= 23 and mes == 8:
    sig = 'leao'
elif dia >= 24 and mes == 8 or dia <= 22 and mes == 9:
    sig = 'virgem'
elif dia >= 23 and mes == 9 or dia <= 23 and mes == 10:
    sig = 'libra'
elif dia >= 24 and mes == 10 or dia <= 22 and mes == 11:
    sig = 'escorpiao'
elif dia >= 23 and mes == 11 or dia <= 21 and mes == 12:
    sig = 'sagitario'
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    sig = 'capricornio'

print(f'{nome}, seu signo é {sig}')