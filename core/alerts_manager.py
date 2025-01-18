class AlertsManager:
    def __init__(self):
        self.alerts = []  # Liste des alertes

    def create_alert(self, symbol: str, condition: str, value: float):
        alert = {"symbol": symbol, "condition": condition, "value": value}
        self.alerts.append(alert)
        return alert

    def list_alerts(self):
        return self.alerts

    def delete_alert(self, index: int):
        if 0 <= index < len(self.alerts):
            return self.alerts.pop(index)
        else:
            raise IndexError("Index invalide")
