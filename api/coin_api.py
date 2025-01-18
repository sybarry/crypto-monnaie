import requests
from config import COINAPI_KEY

BASE_URL = "https://rest.coinapi.io/v1"

def get_current_price(symbol: str) -> float:
    url = f"{BASE_URL}/exchangerate/{symbol}/USD"
    headers = {"X-CoinAPI-Key": COINAPI_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("rate")
    else:
        raise Exception(f"Erreur API : {response.status_code}, {response.text}")
