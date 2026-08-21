# Docker + Flask + PostgreSQL — CRUD de Alunos

Exemplo de uma aplicação web utilizando **Python + Flask + PostgreSQL**, executada com **Docker e Docker Compose**.

A aplicação implementa um CRUD simples de alunos:

```text
Aplicação Flask
      ↓
Docker Compose
      ↓
┌───────────────┐
│     Flask     │
└───────┬───────┘
        │
        ↓
┌───────────────┐
│  PostgreSQL   │
└───────────────┘
```

---

## Como usar

### 1. Criar a pasta do projeto

```bash
mkdir aula-sistemas_internet_docker02
cd aula-sistemas_internet_docker02
```

---

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

Adicione as dependências:

```text
Flask
psycopg2-binary
```

Instale:

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

Crie os arquivos HTML:

```bash
touch templates/base.html
touch templates/index.html
touch templates/alunos.html
touch templates/editar.html
touch templates/cadastrar.html
touch templates/sobre.html
```

A estrutura ficará:

```text
templates/
├── base.html
├── index.html
├── alunos.html
├── editar.html
├── cadastrar.html
└── sobre.html
```

---

### 6. Criar a pasta `static`

```bash
mkdir static
```

Crie o arquivo CSS:

```bash
touch static/style.css
```

---

### 7. Criar a pasta do PostgreSQL

```bash
mkdir postgres
```

Crie o Dockerfile do PostgreSQL:

```bash
touch postgres/Dockerfile
```

---

### 8. Criar o `Dockerfile`

Na raiz do projeto:

```bash
touch Dockerfile
```

Adicione as instruções necessárias para criar a imagem Docker da aplicação Flask.

---

### 9. Criar o `docker-compose.yml`

```bash
touch docker-compose.yml
```

O Compose será utilizado para executar os dois serviços:

```text
flask
postgres
```

---

### 10. Configurar o PostgreSQL

No `docker-compose.yml`, utilize:

```text
Banco: escola
Usuário: admin
Senha: 123456
```

O nome do serviço PostgreSQL será:

```text
postgres
```

Por isso, na aplicação Flask, a conexão deve utilizar:

```python
host="postgres"
```

e não:

```python
host="localhost"
```

---

### 11. Iniciar o PostgreSQL

Inicie somente o banco:

```bash
docker compose up -d postgres
```

Verifique:

```bash
docker compose ps
```

---

### 12. Criar a tabela `alunos`

Entre no PostgreSQL:

```bash
docker compose exec postgres psql -U admin -d escola
```

Execute:

```sql
CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

Verifique as tabelas:

```sql
\dt
```

Verifique os dados:

```sql
SELECT * FROM alunos;
```

Saia:

```sql
\q
```

---

### 13. Criar a imagem da aplicação

Na raiz do projeto:

```bash
docker compose build
```

---

### 14. Iniciar os containers

```bash
docker compose up -d
```

Verifique:

```bash
docker compose ps
```

Os serviços deverão estar em execução:

```text
flask
postgres
```

---

### 15. Acessar a aplicação

Abra o navegador:

```text
http://localhost:5000
```

---

### 16. Testar a conexão com o banco

Acesse:

```text
http://localhost:5000/teste-db
```

A aplicação deverá informar se a conexão com o PostgreSQL foi realizada corretamente.

---

### 17. Listar alunos

Acesse:

```text
http://localhost:5000/alunos
```

A página deverá apresentar os alunos cadastrados no banco.

---

### 18. Cadastrar um aluno

Acesse:

```text
http://localhost:5000/cadastrar
```

Preencha:

```text
Nome
E-mail
```

Envie o formulário.

O aluno deverá ser cadastrado no PostgreSQL.

---

### 19. Verificar o cadastro no banco

Entre no PostgreSQL:

```bash
docker compose exec postgres psql -U admin -d escola
```

Execute:

```sql
SELECT * FROM alunos;
```

Saia:

```sql
\q
```

---

### 20. Editar um aluno

Na página:

```text
http://localhost:5000/alunos
```

Selecione a opção de edição.

Altere os dados e salve.

A aplicação deverá atualizar o registro no PostgreSQL.

---

### 21. Excluir um aluno

Na página:

```text
http://localhost:5000/alunos
```

Selecione a opção de exclusão.

O aluno deverá ser removido do banco de dados.

Atualize a página para verificar.

---

### 22. Verificar os dados no PostgreSQL

Entre novamente no banco:

```bash
docker compose exec postgres psql -U admin -d escola
```

Execute:

```sql
SELECT * FROM alunos;
```

As operações realizadas pela aplicação correspondem a:

```text
INSERT → Cadastro
SELECT → Listagem
UPDATE → Edição
DELETE → Exclusão
```

Saia:

```sql
\q
```

---

### 23. Visualizar os logs

Todos os serviços:

```bash
docker compose logs
```

Acompanhar em tempo real:

```bash
docker compose logs -f
```

Somente Flask:

```bash
docker compose logs -f flask
```

Somente PostgreSQL:

```bash
docker compose logs -f postgres
```

Para sair:

```text
Ctrl + C
```

---

### 24. Parar os containers

```bash
docker compose stop
```

Verifique:

```bash
docker compose ps
```

Os containers estarão parados, mas continuarão existindo.

---

### 25. Iniciar os containers novamente

```bash
docker compose start
```

Verifique:

```bash
docker compose ps
```

Acesse novamente:

```text
http://localhost:5000
```
2. Criar o ambiente virtual Python

Criar o ambiente virtual:

python3 -m venv venv

Ativar o ambiente virtual:

source venv/bin/activate

3. Criar o arquivo de dependências

Criar o arquivo:

touch requirements.txt

Adicionar ao arquivo as dependências utilizadas pelo projeto:

Flask
psycopg2-binary

Instalar as dependências:

pip install -r requirements.txt

4. Criar o arquivo principal da aplicação

Criar o arquivo:

touch app.py

O arquivo app.py será responsável pela aplicação Flask e pelas rotas do sistema.

A aplicação terá as seguintes páginas:

/                 → Página inicial
/alunos           → Lista de alunos
/cadastrar        → Cadastro de aluno
/editar/<id>      → Edição de aluno
/excluir/<id>     → Exclusão de aluno
/sobre            → Página sobre o sistema
/teste-db         → Teste da conexão com PostgreSQL

5. Criar a pasta de templates

Criar a pasta onde ficarão os arquivos HTML:

mkdir templates

Criar os arquivos:

touch templates/base.html
touch templates/index.html
touch templates/alunos.html
touch templates/cadastrar.html
touch templates/editar.html
touch templates/sobre.html

A estrutura ficará:

templates/
├── base.html
├── index.html
├── alunos.html
├── cadastrar.html
├── editar.html
└── sobre.html

O base.html será utilizado como template base para as páginas que utilizarem herança de templates do Flask.
6. Criar a pasta de arquivos estáticos

Criar a pasta:

mkdir static

Criar o arquivo CSS:

touch static/style.css

A estrutura ficará:

static/
└── style.css

7. Criar a pasta do PostgreSQL

Criar uma pasta para os arquivos relacionados ao banco:

mkdir postgres

8. Criar o Dockerfile do PostgreSQL

Criar o Dockerfile:

touch postgres/Dockerfile

Esse arquivo será utilizado para definir a imagem do container PostgreSQL.
9. Criar o Dockerfile do Flask

Na raiz do projeto:

touch Dockerfile

O Dockerfile será responsável por criar a imagem da aplicação Flask.

Ele deverá:

    Utilizar uma imagem base do Python

    Definir o diretório da aplicação

    Copiar o requirements.txt

    Instalar as dependências

    Copiar os arquivos da aplicação

    Expor a porta 5000

    Executar o app.py

10. Criar o Docker Compose

Criar o arquivo:

touch docker-compose.yml

O Docker Compose será utilizado para executar os dois containers da aplicação:

Flask
  ↓
PostgreSQL

Os serviços serão:

flask
postgres

O Compose também criará automaticamente uma rede para que os containers possam se comunicar.
11. Configurar o PostgreSQL

No docker-compose.yml, configurar o PostgreSQL utilizando:

Banco: escola
Usuário: admin
Senha: 123456

O serviço PostgreSQL será identificado dentro da rede Docker pelo nome:

postgres

Por isso, a aplicação Flask deverá utilizar:

host="postgres"

e não:

host="localhost"

Dentro de um container, localhost representa o próprio container.
12. Criar a tabela de alunos

Iniciar somente o container do PostgreSQL:

docker compose up -d postgres

Verificar se está executando:

docker compose ps

Entrar no PostgreSQL:

docker compose exec postgres psql -U admin -d escola

Dentro do PostgreSQL, criar a tabela:

CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

Verificar as tabelas existentes:

\dt

Verificar os dados:

SELECT * FROM alunos;

Para sair do PostgreSQL:

\q

13. Criar a imagem da aplicação Flask

Na raiz do projeto:

docker compose build

Esse comando irá construir a imagem definida no Dockerfile da aplicação Flask.
14. Iniciar os containers

Iniciar os dois serviços:

docker compose up -d

Verificar os containers:

docker compose ps

Deverão aparecer os serviços:

flask
postgres

15. Verificar os logs

Visualizar os logs dos serviços:

docker compose logs

Para acompanhar os logs em tempo real:

docker compose logs -f

Somente os logs do Flask:

docker compose logs -f flask

Somente os logs do PostgreSQL:

docker compose logs -f postgres

Para sair da visualização dos logs:

Ctrl + C

16. Acessar a aplicação

Com os containers executando, acessar:

http://localhost:5000

A página inicial da aplicação deverá ser apresentada.
17. Testar a conexão com o PostgreSQL

A aplicação possui uma rota para verificar a conexão com o banco:

http://localhost:5000/teste-db

Se estiver funcionando corretamente, a aplicação deverá retornar uma mensagem indicando que a conexão com o PostgreSQL foi realizada.
18. Testar a página de alunos

Acessar:

http://localhost:5000/alunos

Essa página executa uma consulta no PostgreSQL e apresenta os alunos cadastrados.

Inicialmente, a tabela poderá estar vazia.
19. Testar o cadastro de alunos

Acessar:

http://localhost:5000/cadastrar

Preencher o formulário com:

Nome
E-mail

Enviar o formulário.

A aplicação executará um INSERT no PostgreSQL e redirecionará para a página de alunos.
20. Verificar o cadastro diretamente no banco

Entrar novamente no PostgreSQL:

docker compose exec postgres psql -U admin -d escola

Executar:

SELECT * FROM alunos;

O aluno cadastrado pela aplicação deverá aparecer no resultado.

Sair:

\q

21. Testar a edição

Na página:

http://localhost:5000/alunos

selecionar a opção de edição de um aluno.

A aplicação deverá abrir:

/editar/<id>

Alterar os dados e salvar.

A aplicação executará um UPDATE no PostgreSQL.

Depois, retornar para:

http://localhost:5000/alunos

e verificar os dados atualizados.
22. Testar a exclusão

Na página de alunos, selecionar a opção de exclusão.

A aplicação executará um DELETE no PostgreSQL.

Depois, atualizar a página:

http://localhost:5000/alunos

O aluno excluído não deverá mais aparecer.
23. Verificar novamente os dados no banco

Entrar no PostgreSQL:

docker compose exec postgres psql -U admin -d escola

Executar:

SELECT * FROM alunos;

Assim é possível verificar diretamente no banco os dados resultantes das operações realizadas pela aplicação.

Sair:

\q

24. Parar os containers

Para parar os containers:

docker compose stop

Verificar:

docker compose ps

Os containers continuarão existindo, mas estarão parados.
25. Iniciar os containers novamente

Para iniciar novamente os containers existentes:

docker compose start

Verificar:

docker compose ps

A aplicação estará novamente disponível em:

http://localhost:5000

26. Parar e remover os containers

Para parar e remover os containers:

docker compose down

Esse comando remove os containers e a rede criada pelo Docker Compose.

Os arquivos do projeto continuam na máquina.
27. Reconstruir a aplicação

Caso o Dockerfile ou os arquivos utilizados para criar a imagem tenham sido alterados, reconstruir a imagem:

docker compose build

Também é possível reconstruir e iniciar os containers em um único comando:

docker compose up -d --build
---

### 26. Remover os containers

```bash
docker compose down
```

Esse comando remove os containers e a rede criada pelo Docker Compose.

Os arquivos do projeto continuam na máquina.

---

### 27. Reconstruir a aplicação

Caso o `Dockerfile` ou `requirements.txt` tenha sido alterado:

```bash
docker compose build
```

Também é possível reconstruir e iniciar os containers em um único comando:

```bash
docker compose up -d --build
```

---

## Estrutura final do projeto

```text
aula-sistemas_internet_docker02/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── postgres/
│   └── Dockerfile
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── alunos.html
│   ├── cadastrar.html
│   ├── editar.html
│   └── sobre.html
│
├── static/
│   └── style.css
│
└── venv/
```

---

## Resumo dos principais comandos

| Comando                            | Função                            |
| ---------------------------------- | --------------------------------- |
| `docker compose build`             | Cria as imagens                   |
| `docker compose up -d`             | Cria e inicia os containers       |
| `docker compose up -d --build`     | Reconstrói e inicia os containers |
| `docker compose ps`                | Lista os serviços                 |
| `docker compose logs`              | Exibe os logs                     |
| `docker compose logs -f`           | Acompanha os logs                 |
| `docker compose stop`              | Para os containers                |
| `docker compose start`             | Inicia containers existentes      |
| `docker compose down`              | Remove containers e rede          |
| `docker compose exec postgres ...` | Acessa o PostgreSQL               |
