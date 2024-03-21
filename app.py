import os
from flask import Flask, request
import requests


app = Flask(__name__)
BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

@app.route('/')
def index():
  return 'Olá, <b>tudo bem?</b>'

@app.route('/teste')
def sobre():
  return 'Sobre o <strong>projeto</strong>'

@app.route('/telegram', methods="POST")
def telegram_update():
  update = request.json
  url_envio_mensagem = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  chat_id = update['message']['chat']['id']
  mensagem = {'chat_id': chat_id, 'text': 'Mensagem <b>recebida</b>', 'parse_mode': 'html'}
  request.post(url_envio_mensagem, data=mensagem)
  return 'ok'