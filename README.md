# Docker + Flask — Aplicação Web Simples

Exemplo básico de uma aplicação web utilizando **Python + Flask** executada dentro de um **container Docker**.

O objetivo deste projeto é demonstrar, de forma simples, o funcionamento básico do Docker:

```text
Aplicação Flask
      ↓
  Dockerfile
      ↓
Imagem Docker
      ↓
Container
      ↓
      ↓
Navegador

# Como usar 

## 1 - Criar a pasta do projeto

mkdir docker-flask
cd docker-flask

## Criar o ambiente virtual Python

python3 -m venv venv

Ative o ambiente virutal criado:

source venv/bin/activate

## 3 - Criar o arquivo requirements.txt

touch requirements.txt

Abra o arquivo e adicione o Flask como dependência, após isso instale as dependências:

pip install -r requirements.txt

## 4 Criar o app.py

toch app.py

Adicione o código da aplicação Flask ao arquivo app.py.

## 5 Criar a pasta templates

mkdir templates

## 6 Criar a página HTML

touch templates/index.html

Adicione o código HTML da página ao arquivo.

## 7 Testar sem Docker

python app.py

Abra no navegador: http://localhost:5000

## 8 Criar o Dockerfile

touch Dockerfile

Adicione as instruções Docker ao arquivo.

## 9 Criar a imagem Docker

Na raíz do projeto, execute:

docker build -t minha-flask .

Verifique se a imagem foi criada:

docker images

Procure pela imagem:

minha-flask

## 10 Criar e executar o container

Execute:

docker run -d -p 5000:5000 --name minha-flask minha-flask

Verfique se o container está exectuando:

docker ps

## 11 Acessar a aplicação

http://localhost:5000

## 12 Visualizar os logs

docker logs minha-flask

Para acompanhar em tempo real:

docker logs -f minha-flask

Para sair:

Crtl + C

## 13 Parar o container

docker stop minha-flask

Verifique:

docker ps

O container não deverá mais aparecer entre os containers em execução.

## 14 Inciar o container novamente (com o docker stop o container ainda continua existindo)

docker start minha-flask
docker ps

Acesse novamente : http://localhost:5000

## 15 Remover o container

Primeiro, pare o container:

docker stop minha-flask

Depois remova:

Docker rm minha-flask

Verifique:

docker ps -a
