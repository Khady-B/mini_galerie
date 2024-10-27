# Mini-Galerie d'Images avec Django

## Installation

1. Clonez le dépôt
2. Installez les dépendances : `pip install -r requirements.txt`
3. Configurez la base de données : `python manage.py migrate`
4. Lancez le serveur : `python manage.py runserver`
5. Lancez Celery : `celery -A mini_galerie worker --loglevel=info`

## Tests

Pour exécuter les tests, utilisez la commande : `python manage.py test`
