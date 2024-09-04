from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detalhes-fisica.html")
def detalhes_fisica():
    return render_template("detalhes-fisica.html")


@app.route("/detalhes-biologia.html")
def detalhes_biologia():
    return render_template("detalhes-biologia.html")


@app.route("/artigo-avancos.html")
def avancos():
    return render_template("artigo-avancos.html")


@app.route("/artigo-aplicacoes.html")
def aplicacoes():
    return render_template("artigo-aplicacoes.html")


@app.route("/artigo-terapia.html")
def terapia():
    return render_template("artigo-terapia.html")


@app.route("/artigo-biotecnologia.html")
def biotecnologia():
    return render_template("artigo-biotecnologia.html")
