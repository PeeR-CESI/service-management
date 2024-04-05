# Utiliser une image Python officielle comme image de base
FROM python:3.12.2

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances dans le répertoire courant du conteneur
COPY requirements.txt .

# Installer les dépendances listées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le dossier src entier dans le répertoire de travail /app du conteneur
COPY src .

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5010

# Définir la variable d'environnement FLASK_APP
ENV FLASK_APP=src/app.py

# Définir la commande pour exécuter l'application Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5010"]