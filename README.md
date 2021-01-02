# DJANGO REST FRAMEWORK + ZAPPA + MYSQL

Restful Serverless Architecture with Zappa

- Python 3.8.6
- [Django](https://docs.djangoproject.com/) 3.1.4
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.12.2
- [Zappa](https://github.com/Miserlou/Zappa) 0.52.0

# Features

- Integrated services for python serverless restful api 
  - Swagger(for API Docs)
  - zappa(for python Serverless)
  - django rest framework(for restful api)
  - Mysql(for relational database)
- Divided settings(base, local, production)

# Getting Started

1. Input credential information into `~/.aws/credentials` file from AWS IAM
   (or if aws cli is installed, run `aws configure`)
    ```text
    [zappa]
    aws_access_key_id = <AWS access key id>
    aws_secret_access_key = <AWS secret access key>
    ```
2. Make database and get endpoint(local, production)
3. Make S3 bucket for static files and allow public access (or use cloud front for cdn)

```shell script
git clone https://github.com/wkdtjsgur100/zappa-drf-mysql.git
# activate virtualenv based on python 3.8.6 if you want
pip install -r requirements.txt
zappa init
python ./setup.py
zappa deploy <my-zappa-stage>
zappa manage <my-zappa-stage> "collectstatic --noinput"
```

# Undeploy

```shell script
zappa undeploy <my-zappa-stage>
```

# Deploy updated code

```shell script
zappa update <my-zappa-stage>
```

# Database Migrate

```shell script
zappa manage dev migrate
```

# Create superuser for admin

```shell script
zappa manage <my-zappa-stage> create_admin_user <nickname> <email> <password>
```

# Swagger

- swagger endpoint: http://localhost:8000/swagger/
- More info: [https://drf-yasg.readthedocs.io/en/stable/](https://drf-yasg.readthedocs.io/en/stable/)

# License

MIT License