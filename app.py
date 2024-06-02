from pytube import YouTube
import tkinter
import customtkinter
import os


def IniciarDownloadMusica():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        musica = ytObject.streams.filter(only_audio=True).first()
        file_path = f"{ytObject.title}.mp3"
        musica.download(output_patch='.', filename=filepatch)
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(
            text='Download Concluído com sucesso!', text_color='green')
    except Exception as e:
        ultimalabel.configure(text=f'Erro: {str(e)}', text_color='red')


def IniciarDownloadVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        file_path = f"{ytObject.title}.mp4"
        video.download(output_path='.', filename=file_path)
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(
            text='Download Concluído com sucesso!', text_color='green')
    except Exception as e:
        ultimalabel.configure(text=f'Erro: {str(e)}', text_color='red')


def on_progress(stream, chunk, bytes_remaining):
    tamanho_total = stream.filesize
    bytes = tamanho_total - bytes_remaining
    porcentagem = bytes / tamanho_total * 100
    por = str(int(porcentagem))
    barra_progresso2.configure(text=por + '%')
    barra_progresso2.update()
    barra_progresso.set(float(porcentagem) / 100)


# < ========== Configs Initials ========== >
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Paneleiros Downloader')
