import tkinter as tk
from tkinter import messagebox
from alerts_manager import AlertsManager
from notifier import start_notifier
import threading

class CryptoNotifierUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Notifier")
        self.alerts_manager = AlertsManager()

        # Frames
        self.setup_ui()

    def setup_ui(self):
        # Create Alert Frame
        self.create_alert_frame = tk.Frame(self.root)
        self.create_alert_frame.pack(pady=10)
        
        tk.Label(self.create_alert_frame, text="Symbole :").grid(row=0, column=0)
        self.symbol_entry = tk.Entry(self.create_alert_frame)
        self.symbol_entry.grid(row=0, column=1)

        tk.Label(self.create_alert_frame, text="Condition :").grid(row=1, column=0)
        self.condition_var = tk.StringVar(value="below")
        tk.OptionMenu(self.create_alert_frame, self.condition_var, "below", "above").grid(row=1, column=1)

        tk.Label(self.create_alert_frame, text="Valeur seuil :").grid(row=2, column=0)
        self.value_entry = tk.Entry(self.create_alert_frame)
        self.value_entry.grid(row=2, column=1)

        tk.Button(self.create_alert_frame, text="Ajouter une alerte", command=self.add_alert).grid(row=3, columnspan=2, pady=10)

        # Alerts List Frame
        self.alerts_list_frame = tk.Frame(self.root)
        self.alerts_list_frame.pack(pady=10)

        self.alerts_listbox = tk.Listbox(self.alerts_list_frame, width=50)
        self.alerts_listbox.pack(side=tk.LEFT)

        tk.Button(self.alerts_list_frame, text="Supprimer l'alerte", command=self.delete_alert).pack(side=tk.RIGHT, padx=10)

        # Start Listener Frame
        self.start_listener_frame = tk.Frame(self.root)
        self.start_listener_frame.pack(pady=10)

        tk.Button(self.start_listener_frame, text="Démarrer l'écoute", command=self.start_listener).pack()

    def add_alert(self):
        symbol = self.symbol_entry.get().strip().upper()
        condition = self.condition_var.get()
        try:
            value = float(self.value_entry.get())
            alert = self.alerts_manager.create_alert(symbol, condition, value)
            self.alerts_listbox.insert(tk.END, f"{alert['symbol']} - {alert['condition']} {alert['value']}")
            self.symbol_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            messagebox.showinfo("Succès", "Alerte ajoutée avec succès.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide.")

    def delete_alert(self):
        selected_index = self.alerts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.alerts_manager.delete_alert(index)
            self.alerts_listbox.delete(index)
            messagebox.showinfo("Succès", "Alerte supprimée avec succès.")
        else:
            messagebox.showwarning("Attention", "Veuillez sélectionner une alerte à supprimer.")

    def start_listener(self):
        threading.Thread(target=start_notifier, args=(self.alerts_manager,), daemon=True).start()
        messagebox.showinfo("Démarré", "Le mécanisme d'écoute a été démarré.")
