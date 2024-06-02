from pytube import YouTube
from pytube.exceptions import PytubeError
import tkinter
import customtkinter
import os

def IniciarDownloadMusica():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        musica = ytObject.streams.filter(only_audio=True).first()
        file_path = f"{ytObject.title}.mp3"
        musica.download(output_path='./musicas', filename=file_path)
        os.rename(file_path, file_path.replace(".mp4", ".mp3"))  # Renomear o arquivo para .mp3
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except PytubeError as e:
        ultimalabel.configure(text=f'Erro Pytube: {str(e)}', text_color='red')

def IniciarDownloadVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        resolucao_video = resolucao_var.get()
        
        # Selecionar stream de vídeo e áudio combinados
        video = ytObject.streams.filter(progressive=True, res=resolucao_video).first()
        
        if not video:
            ultimalabel.configure(text=f'Resolução {resolucao_video} não disponível', text_color='red')
            return
        
        file_path = f"{ytObject.title}.mp4"
        video.download(output_path='./videos', filename=file_path)
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except PytubeError as e:
        ultimalabel.configure(text=f'Erro Pytube: {str(e)}', text_color='red')

# < ========== Configs Iniciais ========== >
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Paneleiros Downloader')
resolucao_var = tkinter.StringVar()

# < ========== TÍTULO DO APP ========== >
titulo = customtkinter.CTkLabel(app, text='Coloque o link da sua música/vídeo que deseja baixar')
titulo.pack(padx=10, pady=10)

var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=var)
link.pack()

ultimalabel = customtkinter.CTkLabel(app, text='')
ultimalabel.pack()

# < ========== BOTÃO DOWNLOAD em formato MP3 ========== >
downloadmusica = customtkinter.CTkButton(app, text='Iniciar Download em MP3', command=IniciarDownloadMusica)
downloadmusica.pack(padx=10, pady=10)

# < ========== BOTÃO DOWNLOAD em formato MP4 ========== >
downloadvideo = customtkinter.CTkButton(app, text='Iniciar Download em MP4', command=IniciarDownloadVideo)
downloadvideo.pack(padx=10, pady=10)

# < ========== DROPDOWN ========== >
resolucao_opcoes = ['1080p', '720p', '480p', '360p', '240p']
resolucao_dropdown = customtkinter.CTkOptionMenu(app, values=resolucao_opcoes, variable=resolucao_var)
resolucao_dropdown.pack()

app.mainloop()
