def exibir_pergunta(pergunta, opcoes, resposta_correta):
    print(pergunta)
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    try:
        resposta_usuario = int(input("Escolha a opção correta (1, 2 ou 3): "))
        if resposta_usuario < 1 or resposta_usuario > 3:
            print("Opção inválida. Tente novamente.")
            return exibir_pergunta(pergunta, opcoes, resposta_correta)
        if opcoes[resposta_usuario - 1] == resposta_correta:
            return True
        else:
            return False
    except ValueError:
        print("Por favor, insira um número válido.")
        return exibir_pergunta(pergunta, opcoes, resposta_correta)


def quiz_programacao():
    perguntas = [
        {
            "pergunta": "Qual é a principal diferença entre uma lista e uma tupla em Python?",
            "opcoes": ["Listas são imutáveis e tuplas são mutáveis.", "Listas são mutáveis e tuplas são imutáveis.", "Não há diferença."],
            "resposta_correta": "Listas são mutáveis e tuplas são imutáveis."
        },
        {
            "pergunta": "O que significa a palavra-chave 'def' em Python?",
            "opcoes": ["Define uma variável", "Define uma função", "Define uma classe"],
            "resposta_correta": "Define uma função"
        },
        {
            "pergunta": "Qual é a saída do código a seguir: print(3 * 2 + 1)?",
            "opcoes": ["7", "5", "6"],
            "resposta_correta": "7"
        },
        {
            "pergunta": "O que faz a função 'len()' em Python?",
            "opcoes": ["Retorna o tamanho de uma lista ou string", "Retorna o tipo de um objeto", "Cria um novo objeto"],
            "resposta_correta": "Retorna o tamanho de uma lista ou string"
        },
        {
            "pergunta": "Como se declara uma variável em Python?",
            "opcoes": ["var = 10", "int var = 10", "10 = var"],
            "resposta_correta": "var = 10"
        },
        {
            "pergunta": "Qual é a estrutura de repetição usada para iterar sobre uma sequência em Python?",
            "opcoes": ["while", "if", "for"],
            "resposta_correta": "for"
        }
    ]
    
    acertos = 0

    for pergunta in perguntas:
        if exibir_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta_correta"]):
            print("Resposta correta!\n")
            acertos += 1
        else:
            print("Resposta incorreta.\n")
    
    total_perguntas = len(perguntas)
    porcentagem = round((acertos / total_perguntas) * 100, 2) 

    print(f"Você acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Sua porcentagem de acertos é: {porcentagem}%")

#Chamando o Funcão
quiz_programacao()
