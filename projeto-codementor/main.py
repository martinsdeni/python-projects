import tkinter as tk
from tkinter import messagebox

# Função para exibir as perguntas e verificar as respostas
def exibir_pergunta(pergunta, opcoes, resposta_correta, index_pergunta):
    pergunta_label.config(text=pergunta)
    for i, opcao in enumerate(opcoes, 1):
        botoes_respostas[i-1].config(text=opcao, command=lambda i=i: verificar_resposta(i, resposta_correta, index_pergunta))

# Função para verificar a resposta
def verificar_resposta(escolha, resposta_correta, index_pergunta):
    global acertos
    if botoes_respostas[escolha - 1].cget("text") == resposta_correta:
        acertos += 1

    index_pergunta += 1

    if index_pergunta < len(perguntas):
        proxima_pergunta(index_pergunta)
    else:
        mostrar_resultado()

# Função para mostrar a próxima pergunta
def proxima_pergunta(index_pergunta):
    pergunta_atual = perguntas[index_pergunta]
    exibir_pergunta(pergunta_atual["pergunta"], pergunta_atual["opcoes"], pergunta_atual["resposta_correta"], index_pergunta)

# Função para exibir o resultado
def mostrar_resultado():
    porcentagem = (acertos / len(perguntas)) * 100
    porcentagem = round(porcentagem, 2)
    messagebox.showinfo("Resultado", f"Você acertou {acertos} de {len(perguntas)} perguntas.\nSua porcentagem de acertos é: {porcentagem}%")
    janela.quit()  # Fecha a janela após mostrar o resultado

# Lista de perguntas e respostas
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

# Configuração da janela principal
janela = tk.Tk()
janela.title("Codementor")

# Configuração do label para a pergunta
pergunta_label = tk.Label(janela, text="", font=("Arial", 14), wraplength=400)
pergunta_label.pack(pady=20)

# Configuração dos botões de respostas
botoes_respostas = []
for _ in range(3):
    botao = tk.Button(janela, text="", width=30, height=2, font=("Arial", 12))
    botoes_respostas.append(botao)
    botao.pack(pady=5)

# Começa com a primeira pergunta
proxima_pergunta(0)

# Inicia a interface gráfica
janela.mainloop()
