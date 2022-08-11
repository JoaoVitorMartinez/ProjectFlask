from flask import Flask, render_template


app = Flask("Projeto")
@app.route("/")
def ola_mundo():
    nome = "Joao"
    produtos = [
        {"nome" : "Caneta", "preco" : 0.99},
         {"nome" : "Xbox One", "preco" : 1600.00}
         ]
     

    return render_template("index.html",n= nome, aProdutos=produtos), 200

app.run()