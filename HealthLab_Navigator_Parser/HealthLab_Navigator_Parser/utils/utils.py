import re
from typing import Union

import requests


def clear_price(old_price_string: str) -> int:
    return int(re.sub(r'[^\d.,]', '', old_price_string))


def clear_string(old_string: str) -> str:
    return old_string.replace('\n', '').strip()


def ai_request(message: str) -> Union[None, str]:
    url = 'https://www.botlibre.com/rest/json/chat'
    headers = {'Content-Type': 'application/json'}
    data = {
        'application': '2227669578165338569',
        'instance': '48333609',
        'message': message
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        if response.json().get('message'):
            return response.json().get('message')
    return None
