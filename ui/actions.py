from tkinter import messagebox
import threading
from core.notifier import start_notifier
import tkinter as tk
from api.coin_api import get_current_price



def add_alert(ui):
    symbol = ui.frames['symbol_entry'].get().strip().upper()
    condition = ui.frames['condition_var'].get()
    try:
        value = float(ui.frames['value_entry'].get())
        alert = ui.alerts_manager.create_alert(symbol, condition, value)
        ui.frames['alerts_listbox'].insert(tk.END, f"{alert['symbol']} - {alert['condition']} {alert['value']}")
        ui.frames['symbol_entry'].delete(0, tk.END)
        ui.frames['value_entry'].delete(0, tk.END)
        messagebox.showinfo("Succès", "Alerte ajoutée avec succès.")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide.")

def update_alerts(ui):
    """Met à jour les alertes et vérifie leurs conditions."""
    try:
        for alert in ui.alerts_manager.list_alerts():
            current_price = get_current_price(alert["symbol"])
            condition_met = (
                (alert["condition"] == "below" and current_price < alert["value"]) or
                (alert["condition"] == "above" and current_price > alert["value"])
            )
            if condition_met:
                messagebox.showinfo(
                    "Alerte déclenchée",
                    f"🔔 {alert['symbol']} est {alert['condition']} {alert['value']}.\nPrix actuel : {current_price}",
                )
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la mise à jour des alertes : {e}")

def delete_alert(ui):
    selected_index = ui.frames['alerts_listbox'].curselection()
    if selected_index:
        index = selected_index[0]
        ui.alerts_manager.delete_alert(index)
        ui.frames['alerts_listbox'].delete(index)
        messagebox.showinfo("Succès", "Alerte supprimée avec succès.")
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner une alerte à supprimer.")

def start_listener(ui):
    threading.Thread(target=start_notifier, args=(ui.alerts_manager,), daemon=True).start()
    messagebox.showinfo("Démarré", "Le mécanisme d'écoute a été démarré.")
