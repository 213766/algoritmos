def lerNotas(aluno: str):
    notas = []
    for i in range(4):
        notas.append(float(input(f'Insira a nota da prova/atividade {i+1}: ')))
    media = sum(notas)/ len(notas)
    return [aluno, media]

aprovados = []

for _ in range(10):
    aluno = lerNotas(input(f'Insira o nome do aluno: '))
    if aluno[1] >= 7.0:
        aprovados.append(aluno)

print(f'LISTA DE ALUNOS APROVADOS:')
for aluno in aprovados:
    print(f'{aluno[0]} Aprovado com média {aluno[1]}')