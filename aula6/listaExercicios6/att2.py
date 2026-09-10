numeros = []

for n in range(10):
    
    while True:
        numInput = input("Insira um numero: ")
        try:
            float(numInput)
            break
        except:
            print(f"ve aí, '{numInput}' nao é numero...")

    numeros.append(float(numInput))

numeros.reverse()
print(numeros)