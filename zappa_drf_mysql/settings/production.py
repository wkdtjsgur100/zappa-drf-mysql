import os

from .base import *

DATABASES = {
    'default' : {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.environ.get('prod_db_name'),
        'USER': os.environ.get('prod_db_user'),
        'PASSWORD': os.environ.get('prod_db_password'),
        'HOST': os.environ.get('prod_db_endpoint'),
        'PORT': os.environ.get('prod_db_port') or '3306',
    }
}

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

cloudfront_url = os.environ.get("cloudfront_url")
AWS_STORAGE_BUCKET_NAME = os.environ.get("s3_bucket")
AWS_S3_REGION_NAME = os.environ.get("AWS_REGION")
AWS_S3_HOST = f"s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_S3_CUSTOM_DOMAIN = cloudfront_url if cloudfront_url else f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_HOST}"
if not cloudfront_url:
    AWS_S3_OBJECT_PARAMETERS = {
        "ACL": "public-read",
    }
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
STATICFILES_STORAGE = "zappa_drf_mysql.storages.ZappaS3Boto3Storage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
DEFAULT_FILE_STORAGE = "zappa_drf_mysql.storages.ZappaS3Boto3Storage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
