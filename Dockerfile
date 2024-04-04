# Utiliser une image Python officielle comme image de base
FROM python:3.12.2

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances dans le répertoire courant du conteneur
COPY requirements.txt .

# Installer les dépendances listées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet dans le conteneur
COPY src/ ./src/
COPY app.py .

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5000

# Définir les variables d'environnement nécessaires pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Définir la commande pour exécuter l'application Flask
CMD ["flask", "run"]