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