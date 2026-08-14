data = input("Insira uma Data(dd/mm/aaaa): ")

dataSeparada = data.split("/")

dia = int(dataSeparada[0])
mes = int(dataSeparada[1])
ano = int(dataSeparada[2])

valido = ano > 0 and ano <= 3000

if valido:

    anoBi = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

    valido = mes > 0 and mes <= 12
    if valido:

        valido = mes in (4,6,9,11) and dia >= 1 and dia <= 30 \
            or mes in (1,3,5,7,8,12) and dia >= 1 and dia <= 31 \
            or anoBi and mes == 2 and dia >= 1 and dia <= 29 \
            or mes == 2 and dia >= 1 and dia <= 28


        if valido:
            print("data valida")
        else:
            print("dia não valido")
            
    else:
        print("Mês Não Valido")
else:
    print("Ano Não Valido")