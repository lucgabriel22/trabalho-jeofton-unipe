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
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except Exception as e:
        ultimalabel.configure(text=f'Erro: {str(e)}', text_color='red')


def IniciarDownloadVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()                