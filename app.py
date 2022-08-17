from distutils.log import debug
from flask import Flask, render_template


app = Flask("Projeto")
@app.route("/")
def main():
    nome = "variável"
    produtos = [
        {"nome" : "Caneta", "preco" : 0.99},
         {"nome" : "Xbox One", "preco" : 1600.00}
         ]
     

    return render_template("index.html",n= nome, aProdutos=produtos), 200

@app.route("/teste")
@app.route("/teste/<var>")
def teste(var=""):
    return "Nova rota teste: {}".format(var), 200


app.run()