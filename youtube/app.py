import os
from tkinter import Tk, Label, Entry, Button, Frame, font
from pytube import YouTube
from flask import Flask, render_template, request

os.environ["DISPLAY"] = ":0.0"

app = Flask(__name__)

HTML_FILE = "index.html"  # Define the constant for the HTML file name

# Disabling CSRF protection for all routes
@app.before_request
def disable_csrf():
    if request.endpoint:
        request.endpoint = request.endpoint.replace('.', '_')
        g.csrf_disable = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form["link"]
        path = request.form["path"]

        try:
            yt = YouTube(link)
            title = "Título: " + yt.title
            views = "Número de views: " + str(yt.views)
            length = "Tamanho do vídeo: " + str(yt.length) + " segundos"
            rating = "Avaliação do vídeo: " + str(yt.rating)

            ys = yt.streams.get_highest_resolution()
            download_label = "Baixando..."
            ys.download(path)
            download_label = "Download completo!"

            return render_template(HTML_FILE, title=title, views=views, length=length, rating=rating, download_label=download_label)
        except Exception as e:
            error_message = "Erro ao baixar o vídeo"
            return render_template(HTML_FILE, error_message=error_message)

    return render_template(HTML_FILE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
