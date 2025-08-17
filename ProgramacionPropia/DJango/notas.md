# Notas de Uso de DJango

## Manejo Entorno Virual

* Comando para crear entornos virtuales `python -m venv [nombre_entorno]`
* activacion de entorno virtual `.\[nombre_entorno]\Scripts\activate`
* cerrar entorno virtual "Sin importar en que carpeta estes" `deactivate`

*Recuerda Instalar Django dentro de este entorno `pip install Django`*

## Manejo de DJango

* Crea el proyecto DJango `django-admin startproject [nombre_proyecto] .` *El punto crea el proyecto en la carpeta que estes ubicado*
* Crea aplicaciones en el proyecto `python manage.py startapp [nombre_aplicacion]`
* Arrancar servidor Django `python manage.py runserver`

## Manejo de DB

* instalar el paquete de comunicacion entre DJango y la Base de datos
  * PostgreSQL: `pip install psycopg2-binary`

    ```
    
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

  * MySQL/MariaDB: `pip install mysqlclient`

    ```
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
