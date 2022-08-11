from flask import Flask

app = Flask("Projeto")
@app.route("/")
def ola_mundo():
    return "Olá mundo Flask!!"

app.run()