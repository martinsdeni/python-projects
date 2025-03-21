#pip install python-barcode pillow pywin32

import tkinter as tk
from tkinter import messagebox
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
import os
import win32print
import win32api 

def gerar_codigo():
    texto = entrada_texto.get()
    if not texto:
        messagebox.showerror("Erro", "Digite um texto para gerar o código de barras.")
        return
    
    try:
        caminho_imagem = os.path.join(os.getcwd(), "codigo_barras")  
        codigo_barras = Code128(texto, writer=ImageWriter())
        codigo_gerado = codigo_barras.save(caminho_imagem)
        caminho_imagem += ".png"  
        exibir_imagem(caminho_imagem)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao gerar código de barras: {e}")

def exibir_imagem(caminho):
    img = Image.open(caminho)
    img.thumbnail((300, 100))  #tam etiqueta
    img = ImageTk.PhotoImage(img)
    label_imagem.config(image=img)
    label_imagem.image = img  
    label_imagem.caminho_imagem = caminho  

def imprimir_codigo():
    if not hasattr(label_imagem, "caminho_imagem"):
        messagebox.showerror("Erro", "Gere um código de barras antes de imprimir.")
        return
    
    printer_name = win32print.GetDefaultPrinter()
    if not printer_name:
        messagebox.showerror("Erro", "Nenhuma impressora padrão encontrada.")
        return
    
    try:
        win32api.ShellExecute(0, "print", label_imagem.caminho_imagem, None, ".", 0)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao imprimir: {e}")

#Interface gráfica
janela = tk.Tk()
janela.title("Gerador de Código de Barras")
janela.geometry("400x300")


frame_topo = tk.Frame(janela)
frame_topo.pack(pady=10)

label_instrucao = tk.Label(frame_topo, text="Digite o texto para o código de barras:")
label_instrucao.pack()

entrada_texto = tk.Entry(frame_topo, width=30)
entrada_texto.pack()

botao_gerar = tk.Button(frame_topo, text="Gerar Código de Barras", command=gerar_codigo)
botao_gerar.pack(pady=5)

label_imagem = tk.Label(janela)
label_imagem.pack()

botao_imprimir = tk.Button(janela, text="Imprimir Código de Barras", command=imprimir_codigo)
botao_imprimir.pack(pady=10)

janela.mainloop()