import psycopg2
from flask import Flask, render_template, request, redirect



app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
        host="postgres",
        database="escola",
        user="admin",
        password="123456"
    )

    return connection



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/alunos")
def alunos():
    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM alunos ORDER BY id;")

    alunos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("alunos.html", alunos=alunos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, email) VALUES (%s, %s)",
            (nome, email)
        )

        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/alunos")

    return render_template("cadastrar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]

        cursor.execute(
            """
            UPDATE alunos
            SET nome = %s, email = %s
            WHERE id = %s
            """,
            (nome, email, id)
        )

        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/alunos")

    cursor.execute(
        "SELECT * FROM alunos WHERE id = %s",
        (id,)
    )

    aluno = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("editar.html", aluno=aluno)

@app.route("/excluir/<int:id>")
def excluir(id):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id = %s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/alunos")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/teste-db")
def teste_db():
    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            current_database(),
            current_schema(),
            inet_server_addr(),
            inet_server_port()
    """)

    resultado = cursor.fetchone()

    cursor.close()
    connection.close()

    return f"""
        Banco: {resultado[0]}<br>
        Schema: {resultado[1]}<br>
        IP: {resultado[2]}<br>
        Porta: {resultado[3]}
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)