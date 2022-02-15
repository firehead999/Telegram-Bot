from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname


app = Flask(__name__)


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # -> API_TOKEN


def send_message(chat_id, text):
    method = 'sendMessage'  #
    token = get_from_env('API_TOKEN')
    url = 'https://api.telegram.org/bot' + token + '/' + method
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)


@app.route('/', methods=['POST'])  # our localhost <- telegram post our messages
def process():
    chat_id = request.json['message']['chat']['id']
    text = 'Hi!'

    send_message(chat_id, text)  # -> post message

    return {'ok': True}


if __name__ == '__main__':
    app.run()
