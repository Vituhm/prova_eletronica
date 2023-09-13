questao1 = {
    "valor_questao": 10,
    "gabarito": "a",
    "enunciado": "Qual é o resultado da soma 10+20?",
    "opcao1": "30",
    "opcao2": "40",
    "opcao3": "50",
    "opcao4": "60"
}
questao2 = {
    "valor_questao": 25,
    "gabarito": "d",
    "enunciado": "Toda potência de expoente zero é igual a ...",
    "opcao1": "0",
    "opcao2": "2",
    "opcao3": "4",
    "opcao4": "1"
}
questao3 = {
    "valor_questao": 15,
    "gabarito": "b",
    "enunciado": "Qual o maior planeta do sistema solar?",
    "opcao1": "Marte",
    "opcao2": "Júpiter",
    "opcao3": "Saturno",
    "opcao4": "Terra"
}
questao4 = {
    "valor_questao": 20,
    "gabarito": "c",
    "enunciado": "Qual a capital do Brasil?",
    "opcao1": "São Paulo",
    "opcao2": "Bahia",
    "opcao3": "Brasília",
    "opcao4": "Goiás"
}
questao5 = {
    "valor_questao": 10,
    "gabarito": "a",
    "enunciado": "Qual a fórmula química da água?",
    "opcao1": "H2O",
    "opcao2": "CO2",
    "opcao3": "NaCl",
    "opcao4": "H2O2"
}

prova = []
gabarito = ['a', 'd', 'b', 'c', 'a']
marcacoes = []
valor_questao = [10, 25, 15, 20, 10]
pontuacao = 0

prova.append(questao1)
prova.append(questao2)
prova.append(questao3)
prova.append(questao4)
prova.append(questao5)

for num, questao in enumerate(prova):
    print(num + 1, ")", questao["enunciado"])
    print("a)", questao["opcao1"])
    print("b)", questao["opcao2"])
    print("c)", questao["opcao3"])
    print("d)", questao["opcao4"])
    print("\n")
    marcacao = input("Digite a letra da resposta escolhida:")
    marcacoes.append(marcacao)

    if marcacao == questao["gabarito"]:
        pontuacao += questao["valor_questao"]

for i in range(0, 5):
    if marcacoes[i] == gabarito[i]:
        print("Questão", i + 1, "correta!")
    else:
        print("Questão", i + 1, "incorreta!", "Questão correta:", gabarito[i])
print(pontuacao)