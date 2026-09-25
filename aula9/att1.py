MES = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

def converterData(data):
    dataSeparada = data.split('/')
    print(dataSeparada)

    dia = int(dataSeparada[0])
    mes = int(dataSeparada[1])
    ano = int(dataSeparada[2])

    return str(dia) + ' de ' + MES[mes-1] + ' de ' + str(ano)

dataConvertida = converterData('24/09/2026')
print(dataConvertida)