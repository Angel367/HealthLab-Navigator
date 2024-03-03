import re


def clear_price(old_price_string: str) -> int:
    return int(re.sub(r'[^\d.,]', '', old_price_string))


def clear_string(old_string: str) -> str:
    return old_string.replace('\n', '').strip()
