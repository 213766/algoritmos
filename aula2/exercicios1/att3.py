def converterKelvin(tempCel):
    return tempCel + 273

tempKel = 0.0
tempCel = 0.0
tempCel = float(input("Insira a temperatura em Celcius: "))

tempKel = converterKelvin(tempCel)

print(f'{tempCel} Celcius em Kelvil são: {tempKel} Kelvin')