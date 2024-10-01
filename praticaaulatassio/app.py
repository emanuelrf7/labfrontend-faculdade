from flask import Flask, render_template
from conferencias import Conferencia
from artigo import Artigo

app = Flask(__name__)

conferencia_list = [
    Conferencia(1, "Tema 1", "Titulo 1", "Descrição 1", "Palestrante 1"),
    Conferencia(2, "Tema 2", "Titulo 2", "Descrição 2", "Palestrante 2"),
    Conferencia(3, "Tema 3", "Titulo 3", "Descrição 3", "Palestrante 3")
]

artigo_list = [
    Artigo(1, "Titulo 1", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nisi aliquam nihil excepturi. Blanditiis eaque, sunt dignissimos culpa soluta odio tenetur, distinctio animi provident ratione accusantium ipsa nostrum quaerat saepe temporibus!"),
    Artigo(2, "Titulo 2", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nisi aliquam nihil excepturi. Blanditiis eaque, sunt dignissimos culpa soluta odio tenetur, distinctio animi provident ratione accusantium ipsa nostrum quaerat saepe temporibus!"),
    Artigo(3, "Titulo 3", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nisi aliquam nihil excepturi. Blanditiis eaque, sunt dignissimos culpa soluta odio tenetur, distinctio animi provident ratione accusantium ipsa nostrum quaerat saepe temporibus!")
]

@app.route("/")
def home():
    return render_template("index.html", conferencia_list=conferencia_list)


@app.route("/conferencia/<int:id>")
def conferencia(id):
    for conferencia in conferencia_list:
        for artigo in artigo_list:
            if artigo.get_id() ==  conferencia.get_id():
                artigo_conferencia = artigo
        
        if conferencia.get_id() == id:
            return render_template("conferencia.html", conferencia=conferencia, artigo_conferencia=artigo_conferencia)
    
    return "<h1>Ops! Nenhuma conferência encontrada!</h1>"


@app.route("/artigo/<int:id>")
def artigo(id):
    for artigo in artigo_list:
        if artigo.get_id() == id:
            return render_template("artigo.html", artigo=artigo)
    
    return "<h1>Ops! Nenhum artigo encontrado!</h1>"