# CI/CD - Web application - Projet Devops
### Auteurs : Keenan Baranès - Maxence Cerfontaine - Thibault Loth
---

### Enoncé : Mettre en place une CI/CD permettant de gérer le cycle vie d'une application WEB : des lancements des tests au déploiement

### Phase 1 : Tests unitaires
---
*Technologies utilisées : Github, Github Action, Application Python, Pytest*

1. Création du fichier [app.py](https://github.com/ThbLoth/CI-CD-dev-web-devops-projet/blob/main/app.py) contenant un serveur Flask et quelques routes pouvant être appellées
2. Création du fichier [/tests/test_app.py](https://github.com/ThbLoth/CI-CD-dev-web-devops-projet/blob/main/tests/test_app.py) permettant de tester la route par défaut (/) en récupérant le contenu de la page.
3. Création du workflow pour github par action contenant les étapes pour les tests unitaires :
   - Vérification du dépot
   - Installation de python 3.8
   - Installation de pip, de Flask et de pytest
   - Vérification de l'installation des dépendances
   - Lancement des tests avec pytests
Si la page est bien en ligne et que le texte affiché sur la page correspond à celui des tests alors la première phase est validée.

---
### Phase 2 : Mise à jour sur une VM de prod
---
*Technologies utilisées : Github action, Azure VM, Ansible*

En amont a été créée et configurée une VM sur Azure à l'aide de nos comptes EFREI. Il s'agit d'une VM Ubuntu classique, accessible en SSH via des clés.
Elle a été configurée pour la suite du projet avec :
- Installation de python, Flask, docker
- Configuration de clés SSH pour communiquer entre Actions et la machine

Pour réaliser cette phase, nous avons suivi le déroulé suivant :
1. Création des fichiers pour ansible [inventory.ini](https://github.com/ThbLoth/CI-CD-dev-web-devops-projet/blob/main/inventory.ini) contenant les informations essentielles pour établir la connexion entre Ansible, Actions et Azure ainsi que le fichier [deploy.yaml](https://github.com/ThbLoth/CI-CD-dev-web-devops-projet/blob/main/deploy.yaml) permettant de copier le fichier de l'application web **app.py** et de l'envoyer sur le répertoire utilisateur sur la VM
2. Dans le workflow ont été ajoutées les étapes suivantes :
   - Test de la connexion à la VM en SSH
   - Installation de Ansible
   - Lancement du playbook Ansible

Si le fichier app.py est bien mis à jour avec la dernière version présente sur Github, alors la seconde phase est validée.

---
###  Phase 3 : Déploiement de l'application via Docker
---
*Technologies utilisées : Docker, Docker Hub, Azure*
Comme dit précédement, Docker tournera sur la VM Azure configurée en amont.

1. Création du [Dockerfile](https://github.com/ThbLoth/CI-CD-dev-web-devops-projet/blob/main/Dockerfile) permettant de récupérer le fichier **app.py** et de créer une image Docker de celle ci.
2. Envoie de l'image devops-project sur Docker Hub
3. (Sur la VM) -> Arrêt et suppression des conteneurs précédents pour permettre la maintenance et le changement de la version qui tourne, tout en évitant ainsi les conflits au niveau des ports utilisés.
4. Pull de l'image sur la VM depuis Docker Hub
5. Lancement du conteneur à l'aide de l'image fraichement téléchargée
6. Application utilisable

---
### Bugs connus
--- 
- L'application n'est accessible que depuis l'intérieur du conteneur (au 25/01/24) --> Probablement un problème de mapping 
