import requests
from api_manager import load_config

def send_telegram(message):
    cfg = load_config()
    token = cfg.get('telegram_token')
    chat_id = cfg.get('telegram_chat_id')
    if not token or not chat_id:
        return
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    try:
        requests.post(url, data=data)
    except:
        pass