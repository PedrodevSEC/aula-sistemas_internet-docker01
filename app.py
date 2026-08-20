from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # 0.0.0.0 é para permitir que a aplicação seja acessada fora do container.
    app.run(host="0.0.0.0", port=5000)