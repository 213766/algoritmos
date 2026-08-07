DIAS_NO_MES = 30
DIAS_NO_ANO = 365

def floor(num: float):
    return int(num)

qtdDias = int(input(f'Insira a quantidade de dias: '))

qtdDiasInput = qtdDias

anos = floor(qtdDias /  DIAS_NO_ANO)
qtdDias = qtdDias - (anos * DIAS_NO_ANO)

meses = floor(qtdDias /  DIAS_NO_MES)
qtdDias = qtdDias - (meses * DIAS_NO_MES)

print(f'{qtdDiasInput} dia(s) equivale a {anos} ano(s), {meses} mês(es) e {qtdDias} dia(s)')