FROM python:3.8

WORKDIR /app

#On copie le fichier app.py dans le conteneur
COPY app.py .

#On installe les dépendances
RUN pip install flask

#On expose le port 5000
EXPOSE 5000

#On lance l'application
CMD ["python", "app.py"]

