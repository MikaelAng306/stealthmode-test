# stealthmode-test
Test technique de la FinTech Stealth Technique

# 🚀 Fonctionnalites
- Endpoints
```
    POST /payments/initiate : Initialisation d'un payement
    GET /payments/verify?transaction_id=<id> : Verification du statut d'un payement
```
- Database: PostgreSQL

- Security: Management des cles API avec les variables d'environnement

- Testing: Unit tests disponibles

# 🐋 Lancement en utilisant Docker

## Prerequisites
    * Docker
    * Docker Compose

## Etapes pour Run avec Docker

- Cloner le repo:
```
git clone <repository-url>
cd <project-directory>
```
- Lancer Docker:
```
docker-compose up --build
```
* APIs sur:

http://localhost:8000

* Pour voir la base de donnee:
    * docker exec -it postgres_db psql -U mike -d stealth_db

# 🐋 Lancement sans Docker

## Prerequisites
    * Python 3.8+
    * PostgrSQL

- Cloner le repo:
```
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
```

- Configurer la base donnee PostgreSQL:

```
sudo -u postgres psql            
CREATE DATABASE stealth_db;
CREATE USER mike WITH PASSWORD 'ASDF_op308';
ALTER ROLE mike SET client_encoding TO 'utf8';
ALTER ROLE mike SET default_transaction_isolation TO 'read committed';
ALTER ROLE mike SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE stealth_db TO mike;
```
- Decommenter le 1er DATABSE dans settings.py

- Run migrations
```
python3 manage.py makemigrations
python3 manage.py migrate

```

- Pour les tests:

```
python3 manage.py test

```

- Lancement du server:

```
python3 manage.py runserver

```

* APIs sur:

http://localhost:8000

# USAGE APIS

- Endpoint: POST /payments/initiate
- Body:
```
{
  "montant": 1000,
  "monnaie": "USD", (## Optionel)
  "email": "mm@gmail.com" (## Optionel)
}
```

- Endpoint: GET /payments/verify?transaction_id=<id>

# USING REST Framework on localhost:8000 to test the endpoints manually or PostMan

## To check database go on localhost:8000/admin
docker exec -it django_app python manage.py createsuperuser
to create a new super user or use this
Username: mike
Password: mikboss306