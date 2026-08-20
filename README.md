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
  Navegador
```

---

## Como usar

### 1. Criar a pasta do projeto

```bash
mkdir docker-flask
cd docker-flask
```

### 2. Criar o ambiente virtual Python

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

---

### 3. Criar o arquivo `requirements.txt`

```bash
touch requirements.txt
```

Abra o arquivo e adicione o Flask como dependência:

```text
Flask
```

Depois, instale as dependências:

```bash
pip install -r requirements.txt
```

---

### 4. Criar o `app.py`

```bash
touch app.py
```

Adicione o código da aplicação Flask ao arquivo `app.py`.

---

### 5. Criar a pasta `templates`

```bash
mkdir templates
```

---

### 6. Criar a página HTML

```bash
touch templates/index.html
```

Adicione o código HTML da página ao arquivo.

---

### 7. Testar a aplicação sem Docker

Execute:

```bash
python app.py
```

Abra o navegador e acesse:

```text
http://localhost:5000
```

Se a aplicação estiver funcionando corretamente, a página Flask será exibida.

---

### 8. Criar o `Dockerfile`

Na raiz do projeto:

```bash
touch Dockerfile
```

Adicione as instruções necessárias para criar a imagem Docker da aplicação.

---

### 9. Criar a imagem Docker

Na raiz do projeto, execute:

```bash
docker build -t minha-flask .
```

Verifique se a imagem foi criada:

```bash
docker images
```

Procure pela imagem:

```text
minha-flask
```

---

### 10. Criar e executar o container

Execute:

```bash
docker run -d -p 5000:5000 --name minha-flask minha-flask
```

Verifique se o container está em execução:

```bash
docker ps
```

---

### 11. Acessar a aplicação

Abra o navegador e acesse:

```text
http://localhost:5000
```

Agora a aplicação Flask estará sendo executada dentro do container Docker.

---

### 12. Visualizar os logs

Para visualizar os logs do container:

```bash
docker logs minha-flask
```

Para acompanhar os logs em tempo real:

```bash
docker logs -f minha-flask
```

Para sair:

```text
Ctrl + C
```

> O `Ctrl + C` interrompe apenas a visualização dos logs. O container continua em execução.

---

### 13. Parar o container

Execute:

```bash
docker stop minha-flask
```

Verifique:

```bash
docker ps
```

O container não deverá mais aparecer entre os containers em execução.

> O container ainda existe, apenas está parado.

---

### 14. Iniciar o container novamente

Como o `docker stop` não remove o container, podemos iniciá-lo novamente:

```bash
docker start minha-flask
```

Verifique:

```bash
docker ps
```

Acesse novamente:

```text
http://localhost:5000
```

---

### 15. Remover o container

Primeiro, pare o container:

```bash
docker stop minha-flask
```

Depois, remova-o:

```bash
docker rm minha-flask
```

Verifique:

```bash
docker ps -a
```

O container `minha-flask` não deverá mais aparecer na lista.

---

## Resumo dos principais comandos

| Comando         | Função                        |
| --------------- | ----------------------------- |
| `docker build`  | Cria uma imagem Docker        |
| `docker images` | Lista as imagens disponíveis  |
| `docker run`    | Cria e executa um container   |
| `docker ps`     | Lista containers em execução  |
| `docker ps -a`  | Lista todos os containers     |
| `docker logs`   | Exibe os logs do container    |
| `docker stop`   | Para um container             |
| `docker start`  | Inicia um container existente |
| `docker rm`     | Remove um container           |
