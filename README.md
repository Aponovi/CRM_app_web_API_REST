# Projet 12 - Epic_Event

![made_with_python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![made_with_django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![made_with_postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)


## Description

L'application Django fourni un ensemble d’endpoints sécurisés pour l’API à l'aide du framework Django REST (avec une base de données PostgreSQL) permettant les opérations CRUD (créer, lire, mettre à jour et supprimer) appliquées aux divers objets CRM.

L'utilisation de cette API nécessite une authentification.

## Installation

Cette API exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de pipenv est recommandé, mais des instuctions utilisant venv et pip sont également fournies plus bas.

### Installation de l'application avec pipenv

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone https://github.com/Aponovi/Epic_Event.git` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/Aponovi/Epic_Event/archive/refs/heads/main.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `$ cd SoftDesk`
3. Installez les dépendances du projet à l'aide de la commande `pipenv install`

### Installation de l'application sans pipenv (avec venv et pip)

1. Cloner ce dépôt de code à l'aide de la commande `$ git clone (https://github.com/Aponovi/Epic_Event.git)` (vous pouvez également télécharger le code [en temps qu'archive zip](https://github.com/Aponovi/Epic_Event/archive/refs/heads/main.zip))
2. Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `$ cd SoftDesk`
3. Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`


## Installation de la base de données

1. Créez une base de donnée PostgreSQL
2. Dans configurez votre BDD dans les settings :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<database_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
 ```
    
  Veillez à remplacer les chevrons (ex: <database_name>) par vos identifiants de BDD.
 
3. Initaliser la BDD et l'administration Django avec `python initial_data.py`

## Utilisation

Une fois que vous avez lancé le serveur avec  `python manage.py runserver`, rendez-vous sur un navigateur web à l'adresse http://localhost:8000/admin/


### Documentation

Disponible sur postman : https://documenter.getpostman.com/view/20943323/UzBju96t
