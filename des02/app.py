from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sand-natural-detalhado.html")
def sand_natural_detalhado():
    return render_template("sand-natural-detalhado.html")

@app.route("/coxinha-detalhado.html")
def coxinha_detalhado():
    return render_template("coxinha-detalhado.html")

@app.route("/empadao-detalhado.html")
def empadao_detalhado():
    return render_template("empadao-detalhado.html")

@app.route("/index.html")
def voltar():
    return render_template("index.html")
