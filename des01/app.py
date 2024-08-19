from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trabalhos.html')
def trabalhos():
    return render_template('trabalhos.html')

@app.route('/index.html')
def home():
    return render_template('index.html')
