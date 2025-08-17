# Notas de Uso de DJango

## Manejo del Entorno Virtual

* Comando para crear entornos virtuales: `python -m venv [nombre_entorno]`
* Activación del entorno virtual:
  * **Windows:** `.\<nombre_entorno>\Scripts\activate`
  * **Linux/macOS:** `source [nombre_entorno]/bin/activate`
* Cerrar entorno virtual (no importa en qué carpeta estés): `deactivate`

*Recuerda instalar Django dentro de este entorno:* `pip install Django`

## Manejo de DJango

* Crea el proyecto Django: `django-admin startproject [nombre_proyecto] .` **El punto** crea el proyecto en la carpeta actual.
* Crea aplicaciones en el proyecto: `python manage.py startapp [nombre_aplicacion]`
* Arrancar el servidor de desarrollo de Django: `python manage.py runserver`

## Manejo de la Base de Datos

* Instala el paquete de comunicación entre Django y la base de datos:

  * **PostgreSQL:** `pip install psycopg2-binary`

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'nombre_de_tu_db',
              'USER': 'tu_usuario',
              'PASSWORD': 'tu_contraseña',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```

  * **MySQL/MariaDB:** `pip install mysqlclient`

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'nombre_de_tu_db',
              'USER': 'tu_usuario',
              'PASSWORD': 'tu_contraseña',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```
