from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")



@app.route("/login.html")
def login():
    return render_template("login.html")


@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")


#@app.route("/pegar_cadstro", method=['POST'])
#def registrarCadastro():



@app.route("/emprestimo.html")
def emprestimo():
    return render_template("emprestimo.html")


@app.route("/confirmacao.html")
def confirmacao():
    return render_template("confirmacao.html")


if __name__ == "__main__":
    app.run(debug=True)
