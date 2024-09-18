from flask import Flask, render_template
from conferencias import Conferencia
from palestrantes import PalestrantesFisica, PalestrantesBiologia

app = Flask(__name__)

conferencia_list = [
    Conferencia(1, "Conferência Internacional de Física", "Física Quântica", "10/10/2024", "detalhes-fisica"),
    Conferencia(2, "Simpósio de Biologia Molecular", "Genética e Biotecnologia", "22/11/2024", "detalhes-biologia")
]

palestrantes_fisica_list = [
    PalestrantesFisica(1, "https://img.freepik.com/fotos-gratis/retrato-de-homem-feliz-e-sorridente_23-2149022620.jpg", "Dr. João Silva", "Especialista em Física Quântica com mais de 20 anos de experiência na área."),    
    PalestrantesFisica(2, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTwcDKNEeRMNkDDy9lf1XUjZ2DtlHPiGWzlw&s", "Dra. Maria Oliveira", "Pesquisadora líder em Experimentos de Física de Partículas.")    
]

palestrantes_biologia_list = [
    PalestrantesBiologia(1, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS019jHGCQ4kvMPVLmaDsY43nKoTO1-HPbrBA&s", "Prof. Ana Costa", "Especialista em Biotecnologia com foco em aplicações terapêuticas."),    
    PalestrantesBiologia(2, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc23ymOjEfmy5kCaX0rn47s9CjaM0bMDOo-A&s", "Dr. Pedro Lima", "Pesquisador em Genética Molecular, com ênfase em genética de populações.")    
]

@app.route("/")
def home():
    return render_template("index.html", conferencia_list=conferencia_list)


@app.route("/detalhes-fisica")
def detalhes_fisica():
    return render_template("detalhes-fisica.html", palestrantes_fisica_list=palestrantes_fisica_list)


@app.route("/detalhes-biologia")
def detalhes_biologia():
    return render_template("detalhes-biologia.html", palestrantes_biologia_list=palestrantes_biologia_list)


@app.route("/artigo-avancos")
def avancos():
    return render_template("artigo-avancos.html")


@app.route("/artigo-aplicacoes")
def aplicacoes():
    return render_template("artigo-aplicacoes.html")


@app.route("/artigo-terapia")
def terapia():
    return render_template("artigo-terapia.html")


@app.route("/artigo-biotecnologia")
def biotecnologia():
    return render_template("artigo-biotecnologia.html")
