import json
import requests
from dotenv import load_dotenv

API_TOKEN = '<Your token>'  # API Token your telegram bot
method = 'setWebhook'

'''
url = https://api.telegram.org/bot<token>/НАЗВАНИЕ_МЕТОДА
'''
url = 'https://api.telegram.org/bot' + API_TOKEN + '/' + method

data = {'url': '<your URL>'}  # -> url: our localhost -> URL

headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
