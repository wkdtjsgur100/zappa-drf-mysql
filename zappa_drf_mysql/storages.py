from storages.backends.s3boto3 import S3Boto3Storage


class ZappaS3Boto3Storage(S3Boto3Storage):
    def _get_security_token(self):
        # https://github.com/jschneier/django-storages/issues/606
        return None
