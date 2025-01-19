# crypto-monnaie

# Pour tester mon application : python3 app.py


# Structure du projet
Le projet est organisé selon une structure modulaire pour favoriser la maintenabilité et la séparation des responsabilités. Voici une description des différents dossiers et fichiers :

1. # app.py
Rôle : Ce fichier constitue le point d'entrée principal de l'application. Il initialise les composants essentiels et démarre l'exécution du programme.

2.  # ui/ (Interface utilisateur)
Contient tous les fichiers relatifs à la gestion de l'interface graphique.
__init__.py : Indique que le dossier est un package Python.
main_frame.py : Définit et gère les widgets (boutons, listes déroulantes, champs texte, etc.) qui composent l'interface utilisateur.
actions.py : Contient les actions ou les callbacks liés aux événements utilisateur (clics, saisies, etc.).
ui_manager.py : Implémente la classe principale CryptoNotifierUI, qui coordonne les différents éléments de l'interface et les relie à la logique métier.

3. # core/ (Logique métier)
Ce dossier regroupe la logique principale de l'application.
__init__.py : Rend le répertoire utilisable comme package.
alerts_manager.py : Gère les conditions et les déclencheurs d'alertes (par exemple, en fonction des variations des cours de crypto-monnaies).
notifier.py : Implémente le mécanisme de notification pour informer l'utilisateur.

4. # api/ (Accès à l'API externe)
Ce dossier contient les composants nécessaires pour interagir avec des services externes.
__init__.py : Fichier pour initialiser le package.
coin_api.py : Gère la connexion et les requêtes vers CoinAPI, un service pour récupérer les données sur les crypto-monnaies.

5. # config.py
Rôle : Centralise la configuration, notamment la clé API nécessaire pour accéder à CoinAPI.
Explication : L'utilisation d'un fichier de configuration permet une gestion centralisée des paramètres, facilitant les modifications sans toucher au code source.

6. # requirements.txt : pip install -r requirements.txt
Rôle : Liste toutes les dépendances Python nécessaires pour faire fonctionner l'application.
Explication : Ce fichier est essentiel pour reproduire l'environnement d'exécution. Il est utilisé par pip pour installer toutes les bibliothèques nécessaires.

# Points forts de cette structure :
Modularité : Les responsabilités sont clairement séparées en différents modules.
Facilité de maintenance : Les modifications dans une partie du projet n'affectent pas directement les autres parties.
Réutilisabilité : Les composants tels que alerts_manager ou coin_api peuvent être réutilisés dans d'autres projets similaires.