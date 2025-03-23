import customtkinter as ctk
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Youtube Mp3 Downloader")
janela.geometry("550x450")

# Criação de texto
label = ctk.CTkLabel(janela, text="Youtube Audio Downloader", font=('Segoe UI', 34, 'bold'))
label.pack(pady=(90, 50)) 

# Criação de Caixa de texto
url_entry = ctk.CTkEntry(janela, placeholder_text="Digite a URL do Video:", width=400, height=40, corner_radius=10)
url_entry.pack(pady=20)

# Criação do texto de sucesso
success_label = ctk.CTkLabel(janela, text="Sucesso!", font=('Segoe UI', 15, 'bold'), fg_color="green", corner_radius=10, width=150, height=25)

# Implementar Código de Downloads
def download_video():
    # Pega a URL digitada na caixa de entrada
    urlyt = url_entry.get()
    
    # Verifica se a URL foi fornecida
    if urlyt:
        yt = YouTube(urlyt, on_progress_callback=on_progress)
        audio = yt.streams.filter(only_audio=True).first()
        
        # Se houver um stream de áudio disponível, faz o download
        if audio:
            print('Downloading Audio...')
            
            # Obtém o diretório de Downloads do usuário
            download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            
            # Baixa o arquivo de áudio na pasta de Downloads
            audio.download(output_path=download_dir, filename=f'{yt.title}.mp4')
            
            # Exibe o texto de sucesso
            success_label.pack(pady=10)
            # Faz o texto desaparecer após 3 segundos (3000 milissegundos)
            janela.after(1500, success_label.pack_forget)
        else:
            print("Áudio não encontrado!")
    else:
        print("Por favor, insira uma URL válida!")

# Botão para download
download_button = ctk.CTkButton(janela, text="Download", command=download_video, height=40, width=200)
download_button.pack(pady=20)

# Final
janela.mainloop()
