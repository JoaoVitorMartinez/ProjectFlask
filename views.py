from http.client import ACCEPTED
import helpers
from importlib.metadata import requires
from flask import send_from_directory
from flask import render_template, request, session, redirect, url_for, flash
from models import Jogos, Usuarios
from app import app, db

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
    lista = Jogos.query.order_by(Jogos.id)
    return render_template("jogos.html", jogos=lista), 200


@app.route('/cadastra')
def cadastraJogo():
    if session["usuario"] == None:
        
        return redirect(url_for('login', next=url_for('cadastraJogo'))), 200
    else:
        
        return render_template("form_jogos.html"), 200
    
@app.route('/editar/<int:id>')
def editar(id):
    jogo = Jogos.query.filter_by(id=id).first()
    nome_arquivo = helpers.recupera_imagem(jogo.id)
       
    return render_template('editar.html', jogo=jogo, capa=nome_arquivo)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']
    
    db.session.add(jogo)
    db.session.commit()
    
    img_path = app.config['IMG_PATH']
    arquivo = request.files['imagem']

    if arquivo:
        arquivo.save(f'{img_path}/capa{jogo.id}.jpg')

    return redirect(url_for('jogos')), 200
    
    


@app.route("/form_jogos", methods=["GET", "POST"])
def formjogos():

    if request.method == "POST":
        nome = request.form["nome"]
        categoria = request.form["genero"]
        console = request.form["console"]

        jogo = Jogos.query.filter_by(nome=nome).first()
        
        if jogo:
            return redirect(url_for('jogos')), 200
        
        novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
        db.session.add(novo_jogo)
        db.session.commit()
        
        jogo = Jogos.query.filter_by(nome=nome).first()
        
        
        arquivo = request.files['imagem']
        arquivo.save(f'img/capa{jogo.id}.jpg')
        
        return redirect(url_for('jogos')), 200
    else:
        return "Não pode chamar GET", 200
    
@app.route('/delete/<int:id>')
def delete(id):
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    
    return redirect(url_for('jogos')), 200



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
    proxima = ''
    if request.args.get("next"):
       proxima = request.args.get("next")
    
        
     
    
    return render_template("login.html", proxima=proxima), 200


@app.route('/login_validar', methods=['POST'])
def login_validar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
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

@app.route('/img/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('img', nome_arquivo)
