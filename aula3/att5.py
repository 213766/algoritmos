idade = int(input("Insira a Idade: "))

if idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade < 10:
    print("Infantil B")
elif idade < 13:
    print("Juvenil A")
elif idade < 17:
    print("Juvenil B")
else:
    print("Adulto")