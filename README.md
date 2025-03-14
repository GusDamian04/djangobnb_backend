# Djangobnb_backend
## Descripción
Este es un prototipo de la pagina web de Airbnb, lo cual se divide en dos partes, FrontEnd y Backend. Este repositorio cuenta con la parte de Backend.
- [Página oficial de AirBnb](https://www.airbnb.mx/)

## Cómo funciona
Esta parte del Backend esta construido con a base de Django, y como gestor de base de datos de esta utilizando PostreSQL. Mencionando que se trabajo tambien don Docker Desktop. Por ello 
cuando se clone este proyecto o si empiezas siguiento el tutorial y deseas trabajar con Docker, debes realziar los siguientes pasos:

1. *Primer paso:*
   - Descargar Docker Desktop de la pagina oficial => [Docker Desktop](https://www.docker.com/).
   - Instalar Docker Desktop.
   - Abrir Docker.

2. *Segundo paso:*
   - Abrir de preferencia GitBash (Si revisaras este proyecto ya creado debes clonarlo en la ubicación donde estara).
   - Estar en la ubicación donde esta/estará el proyecto.
   - Si decides empezar este proyecto, debes crear el proyecto django.
   - Y todo lo que se necesita para trabajar con Docker esta en el archivo de Dockerfile.

3. *Repeticion:*
   - Despues para crear el contenedor se debe colocar el siguiente comando "docker-compose up -build", de esta manera se estará construyendo el proyecto en un contenedor de Docker.
   - Para levantar el proyecto solo se debe realizar el siguiente comando "docker-compose up", de esta manera el proyecto funcionará

# *Extra*
Para realizar las migraciones de django hacia la base de datos se necesita el proyecto ejecutandose, por ello al detener la ejecucion se debe de realizar los siguientes comandos:
   - Para tener el proyecto ejecutandose en segundo plano se realiza el "docker-compose up -d".
   - Para makemigration se realiza la siguiente manera "docker-compose exec web python manage.py makemigrations"
   - Para finalizar el migrate se realiza de la siguiente manera "docker-compose exec web python manage.py migrate"

Estos comandos son a base del video tutorial en el que se baso en este proyecto.

## Video Tutorial

- [Full-Stack Airbnb Clone Tutorial: Django, Django Rest Framework & Next.js | With real-time chat](https://youtu.be/psB9vBxPqvE?si=5hnAWbRLT11kF3i8)
