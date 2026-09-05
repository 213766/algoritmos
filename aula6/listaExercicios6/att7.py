INSTRUCAO = 'Responda EXCLUSIVAMENTE com "S" para sim e "N" para NÃO!'

def fazerPergunta(pergunta):
    while True:
        print(pergunta)
        resposta = input()

        if resposta.upper() in ['S', 'N']:
            return resposta.upper() == 'S'
        else:
            print(INSTRUCAO)


print('Você Será Interrogado.\n' + INSTRUCAO)

respostas = []
perguntas = (
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
)

for pergunta in perguntas:
    respostas.append(fazerPergunta(pergunta))

match sum(respostas):
    case 0:
        elementarMeuCaroWatson = 'Não tem nenhum envolvimento, me diga, o que vc esta fazendo aqui? Inocente'
    case 1:
        elementarMeuCaroWatson = 'Pode se retirar você é Inocente'
    case 2:
        elementarMeuCaroWatson = 'Suspeita'
    case 3:
        elementarMeuCaroWatson = 'Humm... Cúmplice'
    case 4:
        elementarMeuCaroWatson = 'Humm... Cúmplice'
    case 5:
        elementarMeuCaroWatson = 'Você é o Assassino. Guardas prendam-no'

print(elementarMeuCaroWatson)