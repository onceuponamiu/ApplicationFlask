
# Projet d'Aperçu des Prix de Location des maisons

Cette application Flask permet aux utilisateurs de visualiser un aperçu des prix de location de maison par région, en utilisant une base de données SQLite pour la gestion des données. Les utilisateurs peuvent consulter une liste de régions accompagnées des prix moyens de location et accéder à des informations détaillées pour chaque région.

## Pour Commencer

Suivez ces instructions pour installer et exécuter une copie du projet sur votre machine locale à des fins de développement et de test.

### Prérequis

- Assurez-vous que Python est installé sur votre système. Ce projet est compatible avec Python 3.6+ et a été développé avec Python 3.8. Téléchargez Python depuis [python.org](https://www.python.org/downloads/).

### Installation

1. **Cloner le dépôt**

   Clonez le dépôt sur votre machine locale en utilisant Git :

   ```bash
   git clone https://github.com/onceuponamiu/AppFlask.git
   cd AppFlask
   ```

2. **Créer un environnement virtuel**

   Créez un environnement virtuel pour isoler les dépendances du projet :

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

   Installez les dépendances nécessaires à partir du fichier `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

### Initialisation de la Base de Données

Avant de lancer l'application, initialisez la base de données en suivant ces étapes :

```bash
flask run 
firefox http://127.0.0.1:5000/init-db
```

Cette commande crée et remplit les tables de la base de données avec des données issues de `pred-mai-mef-dhup-3.csv`.

### Lancer l'Application

Pour démarrer l'application Flask, utilisez :

```bash
flask run
```

Accédez à [http://127.0.0.1:5000/rental-prices/overview](http://127.0.0.1:5000/rental-prices/overview) pour explorer l'application.

### Explorer l'Application

- Visitez `/rental-prices/overview` pour un aperçu des prix de location par région.
- Cliquez sur une région pour voir des détails sur les prix de location, incluant les prix moyens, minimums et maximums.

## Structure du Projet

- `app.py` : Le script principal de l'application Flask.
- `/templates` : Contient les templates Jinja2 pour les vues.
- `requirements.txt` : Liste des dépendances nécessaires pour le projet.

## Contribuer

Consultez le fichier CONTRIBUTING.md pour les détails sur notre code de conduite et le processus de soumission de pull requests.

## Licence

Ce projet est distribué sous la licence MIT. Consultez le fichier LICENSE.md pour plus de détails.

---

Veillez à remplacer `https://your-repository-url.git` par l'URL de votre dépôt et à ajuster les chemins selon vos besoins. Ajoutez des fichiers `CONTRIBUTING.md` et `LICENSE.md` si nécessaire, ou modifiez cette section en conséquence.
