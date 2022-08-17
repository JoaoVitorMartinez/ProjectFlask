from flask import Flask, render_template, request


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

@app.route("/outra")
@app.route("/outra/<var>")
def outra(var= ""):
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


app.run()