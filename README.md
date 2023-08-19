# Projet Compensatoire Basket Ynov

Le "Projet Compensatoire Basket Ynov" est une plateforme dédiée à l'affichage et à la gestion d'informations sur le basket. Elle utilise l'API [balldontlie.io](http://www.balldontlie.io/) pour récupérer et afficher les données.

## Fonctionnalités

1. **Authentification** :
    - Formulaire de connexion et de création de compte.
    - Restriction d'accès aux contenus pour les utilisateurs non connectés.

2. **Joueurs** :
    - Affichage de cartes avec le nom et le prénom de chaque joueur.
    - Possibilité de cliquer sur une carte pour accéder aux détails du joueur, y compris une carte renseignant le nom de son équipe.

3. **Équipes** :
    - Affichage de cartes avec le nom de chaque équipe.
    - Accès aux détails de l'équipe en cliquant sur une carte, incluant une liste de ses joueurs.

4. **Matchs** :
    - Affichage de cartes avec les abréviations des équipes (home_team "VS" visitor_team) et la date de confrontation.
    - Accès aux détails du match en cliquant sur une carte, incluant des cartes pour les deux équipes qui s'affrontent.

## Prérequis

- Python 3.9+
- Django 3.2+
  
## Installation

Pour installer et exécuter le projet, suivez les étapes ci-dessous :

1. **Clonage du dépôt** :
   
   ```bash
   git clone https://github.com/Affy657/Projet_compensatoire_Basket_Ynov.git
2. **Accédez au dossier du projet** :
    ```bash
   cd Projet_compensatoire_Basket_Ynov
3. **Dépendances** :


    ```bash
    pip install -r requirements.txt
4. **Configuration de la base de données** :

    ```bash
    python manage.py migrate
## Utilisation

    python manage.py runserver

**Le projet sera accessible à l'adresse http://localhost:8000** 


N'hésitez pas à me contacter pour toute question concernant ce projet.





