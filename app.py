from urllib.request import urlretrieve
from wsgiref.util import request_uri
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask("Projeto")
app.secret_key = "asdhiadpjkqw"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = 'localhost',
        database = 'jogoteca'
    )

db = SQLAlchemy(app)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Name %r>' % self.name
    

class Usuario(db.Model):
    usuario = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(50), nullable=False)
    


class Jogo():
    def __init__(self, nome, genero, console) -> None:
        self.nome = nome
        self.genero = genero
        self.console = console
        
class Usuario():
    def __init__(self, usuario, senha) -> None:
        self.usuario = usuario
        self.senha = senha
        
eloisa = Usuario('eloisa', '123')
joao = Usuario('joao', '123')
antonio = Usuario('antonio', '123')
        
usuarios = {
    eloisa.usuario: eloisa,
    antonio.usuario: antonio,
    joao.usuario: joao
    
}


lista = []



@app.route("/")
def main():
    nome = "variável"
    produtos = [
        {"nome": "Caneta", "preco": 0.99},
        {"nome": "Xbox One", "preco": 1600.00}
        
    ]

    session["usuario"] = None
    
    return render_template("index.html", n=nome, aProdutos=produtos), 200


@app.route('/jogos')
def jogos():
    jogo = Jogo("Red Dead Remdeption 2", "Mundo Aberto", "PC / Xbox one X/S")
    lista.append(jogo)
    return render_template("jogos.html", jogos=lista), 200


@app.route('/cadastra')
def cadastraJogo():
    if session["usuario"] == None:
        
        return redirect(url_for('login', next=url_for('cadastraJogo'))), 200
    else:
        
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
    proxima='/'
    if request.args.get("next"):
        proxima = request.args.get("next")
    
    return render_template("login.html", proxima=proxima), 200


@app.route('/login_validar', methods=['POST'])
def login_validar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form["usuario"]]
        if request.form['senha'] == usuario.senha:
            proxima_pagina = request.form["proxima"]
            session['usuario'] = request.form['usuario']
            
            flash("Usuário autenticado.")

            return redirect(proxima_pagina)
    
        
    flash("Usuário/senha incorretos.")

    return  render_template("login.html"), 200 


@app.route('/restrito')
def acesso_restrito():
    if session["codigo"] == 1:
        
        return redirect("/jogos"), 200
    else:
        return  200
    
@app.route('/logout')
def logout():
    flash(" saiu.")
    session["usuario"] = None
    session["senha"] = None
    session["codigo"] = None
    
    return render_template("login.html"), 200


app.run()
