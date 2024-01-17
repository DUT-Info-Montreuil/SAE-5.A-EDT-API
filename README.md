<div align="center">

# Gestionnaire EDT - API

**Un site web d'édition d'emploi du temps pour IUT.**<br/>
[Revenir au repo principal](https://github.com/DUT-Info-Montreuil/SAE-5.A-EDT)<br/>

![SQLAlchemy Badge](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=fff&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Flask Badge](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)
![Pytest Badge](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=fff&style=for-the-badge)
![JSON Web Tokens Badge](https://img.shields.io/badge/JSON%20Web%20Tokens-000?logo=jsonwebtokens&logoColor=fff&style=for-the-badge)
</div>

## 🐳 Comment lancer l'application ?

Prérequis :
- Installer [Docker](https://docs.docker.com/engine/install/)

Pour lancer l'application, il vous suffit d'exécuter cette commande :

    docker compose up --build

Il est aussi possible de lancer l'application sans Docker, cependant, elle ne serait pas en capacité de communiquer avec le front. Vous pourrez cependant effectuer les appels API en local à l'aide de Postman. Rendez-vous dans le dossier config.ini et changez son contenu pour ces valeurs.

    [postgresql]
    host=localhost
    database=university
    user=university_admin
    password=password
    
    [server]
    host=localhost
    port=5050
    debug=True

Pour exécuter les tests unitaires, il faut tout d'abord installer les dépendances.

    pip install -r requirements.txt

Puis, il vous suffira de vous rendre dans le dossier tests et d'exécuter pytest.

    cd tests
    pytest

## 👷 Architecture du projet

Les routes de l'API se trouvent dans le dossier "controller", définissant ainsi la gestion des requêtes HTTP. En parallèle, le dossier "service" abrite les fonctionnalités métier de l'API, permettant une séparation entre la gestion des routes et la logique métier.


Le dossier "entities" contient les modèles SQLAlchemy, centralisant la gestion des entités et de la base de données associée.

## 🔒 Sécurité

> [!IMPORTANT]
> **Cela ne sera plus nécessaire après la semaine de refactoring. Ces informations seront intégrées en tant que variables d'environnement.**

@to-write : changer password admin<br/>
@to-write : changer token jwt<br/>
@to-write : changer password postgresql<br/>


## 📎Documentation

- [Swagger](https://github.com/DUT-Info-Montreuil/SAE-5.A-EDT-API/blob/develop/static/swagger.json)
- [Postman](https://github.com/DUT-Info-Montreuil/SAE-5.A-EDT-API/blob/develop/static/EDT.postman_collection.json)

## 🔗 Liens

Repositories :<br/>
- [Principal](https://github.com/DUT-Info-Montreuil/SAE-5.A-EDT)
- [Front](https://github.com/DUT-Info-Montreuil/SAE-5.A-EDT-Front)

## 🔎 Convention de code
  Projet réalisé dans le respect de l'architecture [gitflow](https://danielkummer.github.io/git-flow-cheatsheet/index.fr_FR.html) et des [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)

## 🚶 Participants

- [@Aldriculteur](https://github.com/Aldriculteur) - Aldric CLAUDE
- [@Lony027](https://github.com/Lony027) - Hugo COHEN
- [@adil93s](https://github.com/adil93s) - Adil CHETOUANI
- [@MehediT](https://github.com/MehediT) - Mehedi TOURE
- [@bseydi](https://github.com/bseydi) - Boulaye SEYDI
