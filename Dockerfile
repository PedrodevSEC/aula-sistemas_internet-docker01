# Imagem base
FROM python:3.12-slim 

# Definição do diretório base dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Executa o comando para instalar as dependências apresentadas dentro do arquivo requirements.txt
RUN pip install -r requirements.txt

# Copia tudo do diretório local para o diretório /app dentro do container
COPY . .

# Porta que será exposta
EXPOSE 5000

# Comando que será executado quando o container iniciar
CMD ["python", "app.py"]