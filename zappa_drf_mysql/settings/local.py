import json

from .base import *

with open("config.json", "r") as f:
    # SECURITY WARNING: keep the secret key used in production secret!
    config = json.load(f)
    SECRET_KEY = config.get("DJANGO_SECRET_KEY")

    DATABASES = {
        'default' : {
            'ENGINE': 'mysql.connector.django',
            'NAME': config.get("local_db_name", "database"),
            'USER': config.get("local_db_user", "root"),
            'PASSWORD': config.get("local_db_password", ""),
            'HOST': '127.0.0.1',
            'PORT': config.get("local_db_port", '3306'),
        }
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

