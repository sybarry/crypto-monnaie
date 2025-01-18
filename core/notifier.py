import time
from api.coin_api import get_current_price

def start_notifier(alerts_manager):
    print("Mécanisme d'écoute démarré...")
    while True:
        for alert in alerts_manager.list_alerts():
            try:
                current_price = get_current_price(alert["symbol"])
                condition_met = (
                    (alert["condition"] == "below" and current_price < alert["value"]) or
                    (alert["condition"] == "above" and current_price > alert["value"])
                )
                if condition_met:
                    print(f"🔔 Alerte déclenchée : {alert['symbol']} {alert['condition']} {alert['value']} (Prix actuel : {current_price})")
            except Exception as e:
                print(f"Erreur lors de la vérification : {e}")
        time.sleep(10)
