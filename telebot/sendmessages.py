import os
import requests
from .models import TgSettings
# from dotenv import load_dotenv
# load_dotenv()

# TOKEN = os.environ.get("TOKEN")
# CHAT_ID = os.environ.get("CHAT_ID")


def send_message(name, phone):
    settings = TgSettings.objects.first()
    if settings:
        token = settings.tg_token
        chat_id = settings.tg_chat_id
        text = settings.tg_message

        url = f'https://api.telegram.org/bot{token}/sendMessage'
        msg = text.replace('{name}', name).replace('{phone}', phone)
        try:
            response = requests.post(url, data={'chat_id': chat_id, 'text': msg})
            if response.status_code != 200:
                print(response.text)
                raise Exception
        except Exception as e:
            print(e)

