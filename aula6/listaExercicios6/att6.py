MESES = (
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
)

temperaturas = {}
mesesAcimaMedia = {}

for mes in MESES:
    temperatura = float(input(f'Insira a temperatura do mês de {mes}: '))
    temperaturas.update({mes: temperatura})

valTemperaturas = temperaturas.values()
media = sum(valTemperaturas) / len(valTemperaturas)

for mes in temperaturas:
    temperatura = temperaturas[mes]
    if temperatura > media:
        mesesAcimaMedia.update({mes: temperaturas[mes]})

print(f'MESES COM TEMPERATURAS ACIMA DA MÉDIA ANUAL ({media}):')
for mes in mesesAcimaMedia:
    print(f'{mes} com {mesesAcimaMedia[mes]} graus')