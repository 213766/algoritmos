def converterHora(hora, minuto):
    if hora >= 12:
        padrao = 'PM'
        hora -= 12
    else:
        padrao = 'AM'

    return str(hora) + ':' + str(minuto) + ' ' + padrao

print(converterHora(4,25))