from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Olá, <b>tudo bem?</b>'

@app.route('/sobre')
def sobre():
  return 'Sobre o <strong>projeto</strong>'