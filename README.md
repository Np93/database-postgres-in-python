petite database en python

dans le fichier courant (la ou il y a le docker-compose) lancer avec la commande:

docker-compose up --build


pour tester utiliser une page internet avec cette url: http://localhost:8000/docs#/
bien sur une fois le docker lancer.

il dois y avoir un fichier .env dans le fichier courant pour lancer il doit resembler a ca:

POSTGRES_USER=root
POSTGRES_PASSWORD=pswd
POSTGRES_DB=test
POSTGRES_HOST=postgres

DATABASE_URL=postgres://root:pswd@postgres:5432/test