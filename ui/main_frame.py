import tkinter as tk

def setup_ui(ui):
    """Configure les widgets et frames de l'interface."""
    # Frame pour créer des alertes
    ui.frames['create_alert_frame'] = tk.Frame(ui.root)
    ui.frames['create_alert_frame'].pack(pady=10)

    tk.Label(ui.frames['create_alert_frame'], text="Symbole :").grid(row=0, column=0)
    ui.frames['symbol_entry'] = tk.Entry(ui.frames['create_alert_frame'])
    ui.frames['symbol_entry'].grid(row=0, column=1)

    tk.Label(ui.frames['create_alert_frame'], text="Condition :").grid(row=1, column=0)
    ui.frames['condition_var'] = tk.StringVar(value="below")
    tk.OptionMenu(ui.frames['create_alert_frame'], ui.frames['condition_var'], "below", "above").grid(row=1, column=1)

    tk.Label(ui.frames['create_alert_frame'], text="Valeur seuil :").grid(row=2, column=0)
    ui.frames['value_entry'] = tk.Entry(ui.frames['create_alert_frame'])
    ui.frames['value_entry'].grid(row=2, column=1)

    ui.frames['add_alert_button'] = tk.Button(ui.frames['create_alert_frame'], text="Ajouter une alerte")
    ui.frames['add_alert_button'].grid(row=3, columnspan=2, pady=10)

    # Frame pour la liste des alertes
    ui.frames['alerts_list_frame'] = tk.Frame(ui.root)
    ui.frames['alerts_list_frame'].pack(pady=10)

    ui.frames['alerts_listbox'] = tk.Listbox(ui.frames['alerts_list_frame'], width=50)
    ui.frames['alerts_listbox'].pack(side=tk.LEFT)
    
    ui.frames['update_alert_button'] = tk.Button(ui.frames['alerts_list_frame'], text="Mettre à jour")
    ui.frames['update_alert_button'].pack(side=tk.RIGHT, padx=10)

    ui.frames['delete_alert_button'] = tk.Button(ui.frames['alerts_list_frame'], text="Supprimer l'alerte")
    ui.frames['delete_alert_button'].pack(side=tk.RIGHT, padx=10)

    # Frame pour démarrer le mécanisme d'écoute
    ui.frames['start_listener_frame'] = tk.Frame(ui.root)
    ui.frames['start_listener_frame'].pack(pady=10)

    ui.frames['start_listener_button'] = tk.Button(ui.frames['start_listener_frame'], text="Démarrer l'écoute")
    ui.frames['start_listener_button'].pack()
