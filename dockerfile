FROM python:3.8-buster

# Instala as dependências do Tkinter e do servidor X
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    libx11-6

# Define a variável de ambiente para o display
ENV DISPLAY=:0

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY app.py /app/app.py
COPY templates /app/templates
COPY neymar.jpg /app/neymar.jpg

# Instala as dependências
RUN pip install pytube flask gunicorn

# Define o comando de execução
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
