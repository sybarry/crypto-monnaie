import tkinter as tk
from ui.main_frame import setup_ui
from ui.actions import add_alert, delete_alert, start_listener, update_alerts
from core.alerts_manager import AlertsManager

class CryptoNotifierUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Notifier")
        self.alerts_manager = AlertsManager()

        # Frames et widgets
        self.frames = {}
        setup_ui(self)

    def set_event_handlers(self):
        """Configure les actions des boutons."""
        self.frames['add_alert_button'].config(command=lambda: add_alert(self))
        self.frames['update_alert_button'].config(command=lambda: update_alerts(self))  # Nouveau bouton
        self.frames['delete_alert_button'].config(command=lambda: delete_alert(self))
        self.frames['start_listener_button'].config(command=lambda: start_listener(self))
