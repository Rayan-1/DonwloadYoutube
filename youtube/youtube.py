import os
from tkinter import Tk, Label, Entry, Button, Frame, font
from pytube import YouTube

os.environ["DISPLAY"] = ":0.0"

def download_video():
    link = link_entry.get()
    path = path_entry.get()

    try:
        yt = YouTube(link)
        title_label.config(text="Título: " + yt.title)
        views_label.config(text="Número de views: " + str(yt.views))
        length_label.config(text="Tamanho do vídeo: " + str(yt.length) + " segundos")
        rating_label.config(text="Avaliação do vídeo: " + str(yt.rating))

        ys = yt.streams.get_highest_resolution()
        download_label.config(text="Baixando...")
        ys.download(path)
        download_label.config(text="Download completo!")

    except Exception as e:
        download_label.config(text="Erro ao baixar o vídeo")

# Cria a janela principal
window = Tk()
window.title("Download de Vídeo")
window.geometry("800x700")

# Define a cor de fundo da janela
window.configure(bg="black")

# Cria um quadro centralizado com fundo preto
frame = Frame(window, bg="black")
frame.pack(pady=100)

# Cria os elementos da interface dentro do quadro
link_label = Label(frame, text="Link do vídeo:", bg="black", fg="white", font=("Arial", 14))
link_label.grid(row=0, column=0, padx=20, pady=20, sticky="e")
link_entry = Entry(frame, font=("Arial", 14))
link_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

path_label = Label(frame, text="Local para salvar:", bg="black", fg="white", font=("Arial", 14))
path_label.grid(row=1, column=0, padx=20, pady=20, sticky="e")
path_entry = Entry(frame, font=("Arial", 14))
path_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

download_button = Button(frame, text="Baixar", command=download_video, bg="#007bff", fg="#FFFFFF", font=("Arial", 16, "bold"))
download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

title_label = Label(frame, text="", bg="black", fg="white", font=("Arial", 12))
title_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

views_label = Label(frame, text="", bg="black", fg="white", font=("Arial", 12))
views_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

length_label = Label(frame, text="", bg="black", fg="white", font=("Arial", 12))
length_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

rating_label = Label(frame, text="", bg="black", fg="white", font=("Arial", 12))
rating_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

download_label = Label(frame, text="", bg="black", fg="white", font=("Arial", 12))
download_label.grid(row=7, column=0, columnspan=2)

Tk().withdraw()

# Inicia o loop principal da janela
window.mainloop()
