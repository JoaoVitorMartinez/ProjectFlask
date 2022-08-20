from urllib.request import urlretrieve
from wsgiref.util import request_uri
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask("Projeto")
app.secret_key = "asdhiadpjkqw"


class Jogo():
    def __init__(self, nome, genero, console) -> None:
        self.nome = nome
        self.genero = genero
        self.console = console


lista = []


@app.route("/")
def main():
    nome = "variável"
    produtos = [
        {"nome": "Caneta", "preco": 0.99},
        {"nome": "Xbox One", "preco": 1600.00}
    ]

    return render_template("index.html", n=nome, aProdutos=produtos), 200


@app.route('/jogos')
def jogos():
    jogo = Jogo("Red Dead Remdeption 2", "Mundo Aberto", "PC / Xbox one X/S")
    lista.append(jogo)
    return render_template("jogos.html", jogos=lista), 200


@app.route('/cadastra')
def cadastraJogo():
    return render_template("form_jogos.html"), 200


@app.route("/form_jogos", methods=["GET", "POST"])
def formjogos():

    if request.method == "POST":
        nome = request.form["nome"]
        genero = request.form["genero"]
        console = request.form["console"]

        novoJogo = Jogo(nome, genero, console)
        lista.append(novoJogo)

        return render_template("jogos.html", jogos=lista), 200
    else:
        return "Não pode chamar GET", 200


@app.route("/teste")
@app.route("/teste/<var>")
def teste(var=""):
    return "Nova rota teste: {}".format(var), 200


@app.route("/outra")
@app.route("/outra/<var>")
def outra(var=""):
    return "Var: {}".format(var), 200

# Rota formulário


@app.route("/form")
def form():
    return render_template("form.html"), 200

# Rota tratamento do formulário


@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET", 200


@app.route('/login')
def login():
    return render_template("login.html"), 200


@app.route('/login_validar', methods=['POST'])
def login_validar():
    if request.form["usuario"] == "joao" and request.form["senha"] == "123":
        session["usuario"] = request.form["usuario"]
        session["senha"] = request.form["senha"]
        session["codigo"] = 1

        return redirect(url_for("acesso_restrito"))
    else:

        return "login/senha inválidos", 200


@app.route('/restrito')
def acesso_restrito():
    if session["codigo"] == 1:
        return "<br>Logado</br><br>Login: {}</br><br>Codigo: {}</br>".format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido", 200


app.run()
