# Projet d'Aperçu des Prix de Location

Cette application Flask fournit un aperçu des prix de location par région, en utilisant une base de données SQLite pour stocker et gérer les données. Les utilisateurs peuvent voir une liste des régions avec les prix moyens de location et obtenir des informations détaillées sur les prix pour chaque région.

## Pour Commencer

Ces instructions vous permettront d'obtenir une copie du projet fonctionnelle sur votre machine locale pour le développement et les tests.

### Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre système. Ce projet a été développé avec Python 3.8+, mais il devrait fonctionner avec n'importe quelle version de Python 3.6+. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).

### Installation

1. **Cloner le dépôt**

   Tout d'abord, clonez ce dépôt sur votre machine locale en utilisant Git :

   ```bash
   git clone https://your-repository-url.git
   cd your-project-directory
   ```

2. **Créer un environnement virtuel**

   Il est recommandé de créer un environnement virtuel pour gérer les dépendances du projet séparément des paquets Python de votre système :

   ```bash
   python3 -m venv venv
   ```

   Activez l'environnement virtuel :

   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

3. **Installer les dépendances**

   Installez les dépendances du projet en utilisant le fichier `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

### Initialisation de la Base de Données

Avant de lancer l'application pour la première fois, initialisez la base de données et chargez-la avec des données d'exemple à partir d'un fichier CSV :

```bash
flask run /init-db
```

== CHANGEMENT ICI ===
```bash
flask run 
firefox http://127.0.0.1:5000/init-db
```



Cette commande crée les tables de la base de données et les remplit avec des données de `pred-mai-mef-dhup-3.csv`.

### Lancer l'Application

Pour démarrer l'application Flask, utilisez la commande suivante :

```bash
flask run
```

L'application sera accessible à [http://127.0.0.1:5000/rental-prices/overview](http://127.0.0.1:5000/rental-prices/overview).

### Explorer l'Application

- Naviguez vers `/rental-prices/overview` pour voir un aperçu des prix de location par région.
- Cliquez sur n'importe quelle région pour voir des informations détaillées sur les prix de location, y compris les prix moyens, minimums et maximums.

## Structure du Projet

- `app.py` : Le fichier principal de l'application Flask.
- `/templates` : Contient les modèles Jinja2 pour les vues de l'application.
- `requirements.txt` : Une liste des dépendances de paquets Python pour le projet.

## Contribuer

Veuillez lire CONTRIBUTING.md pour les détails sur notre code de conduite, et le processus pour soumettre des pull requests à nous.

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE.md pour les détails.

---

Assurez-vous de remplacer `https://your-repository-url.git` par l'URL réelle de votre dépôt Git et d'ajuster les chemins des dossiers selon le besoin. Si vous n'avez pas de fichiers `CONTRIBUTING.md` et `LICENSE.md`, envisagez de les ajouter ou de modifier le README en conséquence.
