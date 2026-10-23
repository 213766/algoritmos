alunos = {
    "Ana": {"nota1": 8.5, "nota2": 7.0},
    "Bruno": {"nota1": 5.0, "nota2": 6.5},
    "Carla": {"nota1": 9.0, "nota2": 9.5},
    "Diego": {"nota1": 6.0, "nota2": 4.5},
    "Eduardo": {"nota1": 8.0, "nota2": 6.0},
    "Fernanda": {"nota1": 7.5, "nota2": 8.0},
    "Gabriel": {"nota1": 4.0, "nota2": 5.5},
    "Helena": {"nota1": 9.5, "nota2": 8.5},
    "Igor": {"nota1": 6.5, "nota2": 7.0},
    "Juliana": {"nota1": 8.0, "nota2": 9.0},
    "Lucas": {"nota1": 3.5, "nota2": 6.0},
    "Mariana": {"nota1": 7.0, "nota2": 7.5},
    "Nicolas": {"nota1": 5.5, "nota2": 4.0},
    "Patricia": {"nota1": 10.0, "nota2": 9.0},
    "Rafael": {"nota1": 6.0, "nota2": 8.0}
}

# A)
alunoConsulta = 'ana'
notasAluna = alunos[alunoConsulta.title()]
i = 1
print(f'notas do(a) {alunoConsulta.title()}:')
for nota in notasAluna.values():
    print(f'nota {i}: {nota}')
    i += 1

# B)
alunoConsulta = 'bruno'
notaAlterar = 'nota2'
novaNota = 7.5
print(f'{notaAlterar} antiga do {alunoConsulta.title()}: {alunos[alunoConsulta.title()][notaAlterar]}')
alunos[alunoConsulta.title()][notaAlterar] = novaNota
print(f'{notaAlterar} nova do {alunoConsulta.title()}: {alunos[alunoConsulta.title()][notaAlterar]}')

# C)
nomeNovoAluno = 'Eduardo'
novoAluno = {
    'nota1': 8.0,
    'nota2': 6.0
}
alunos[nomeNovoAluno.title()] = novoAluno

# D)
medias = {}
for aluno, notas in alunos.items():
    contNotas = 0
    somaNota = 0
    for nota in notas.values():
        contNotas += 1
        somaNota += nota
    mediaNota = somaNota / contNotas
    medias[aluno] = mediaNota

# E)
print('Aprovados:')
for aluno, media in medias.items():
    if media >= 7.0:
        print(f'{aluno}: {media}')

# F)
alunoMelhorNota = ''
maiorMedia = 0
for aluno, media in medias.items():
    if media > maiorMedia:
        alunoMelhorNota = aluno
        maiorMedia = media
print(f'Aluno com melhor media: {alunoMelhorNota}, media: {medias[alunoMelhorNota]}')

# G)
somaMedias = 0
contMedias = 0
for media in medias.values():
    contMedias += 1
    somaMedias += media
print(f'media geral da turma: {round(somaMedias / contMedias, 1)}')