# Imagem base
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia a aplicação Flask
COPY app.py .

# Copia os templates e arquivos estáticos
COPY templates/ templates/
COPY static/ static/

# Porta utilizada pelo Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]