salario = float(input("Insira o Salário: "))
cargo = input("insira o cargo: ")
cargo = cargo.lower()

match cargo:
    case "gerente":
        salarioNovo = salario * 1.1
    case "engenheiro":
        salarioNovo = salario * 1.2
    case "engenheiro":
        salarioNovo = salario * 1.3
    case _:
        salarioNovo = salario * 1.4

print(f"Salario antigo: {salario}, salario novo: {salarioNovo}")