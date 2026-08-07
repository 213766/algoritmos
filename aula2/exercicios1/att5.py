volumeGarrCervMl = 600
garrasPorCaixa = 24

caixasConsumidas = int(input('Quantidade de caixas consumidas: '))

volumeConsumidoL = (caixasConsumidas * volumeGarrCervMl) / 1000

print(f'Foram consumidos {volumeConsumidoL} litros de cerveja.')