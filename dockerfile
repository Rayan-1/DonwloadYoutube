FROM python:3.8-slim-buster

# Instala as dependências do Tkinter e do servidor X
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    libx11-6

# Define a variável de ambiente para o display
ENV DISPLAY=:0

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo necessário para o diretório de trabalho
COPY youtube.py /app/youtube.py

# Instala as dependências
RUN pip install pytube

# Define o comando de execução
CMD ["python", "/app/youtube.py"]
