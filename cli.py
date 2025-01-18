from alerts_manager import AlertsManager
from notifier import start_notifier

def display_menu():
    print("\n=== Menu Principal ===")
    print("1. Créer une alerte")
    print("2. Lister les alertes")
    print("3. Supprimer une alerte")
    print("4. Démarrer le mécanisme d'écoute")
    print("5. Quitter")

def run_cli():
    alerts_manager = AlertsManager()

    while True:
        display_menu()
        choice = input("Entrez votre choix : ")

        if choice == "1":
            symbol = input("Entrez le symbole (ex. BTC) : ")
            condition = input("Condition (below/above) : ")
            value = float(input("Entrez la valeur seuil : "))
            alert = alerts_manager.create_alert(symbol, condition, value)
            print(f"Alerte créée : {alert}")

        elif choice == "2":
            alerts = alerts_manager.list_alerts()
            if alerts:
                for i, alert in enumerate(alerts):
                    print(f"{i}. {alert['symbol']} - {alert['condition']} {alert['value']}")
            else:
                print("Aucune alerte disponible.")

        elif choice == "3":
            index = int(input("Entrez l'index de l'alerte à supprimer : "))
            try:
                deleted_alert = alerts_manager.delete_alert(index)
                print(f"Alerte supprimée : {deleted_alert}")
            except IndexError:
                print("Index invalide.")

        elif choice == "4":
            start_notifier(alerts_manager)

        elif choice == "5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")
