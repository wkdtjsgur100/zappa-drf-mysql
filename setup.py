import json

import boto3
import random

secret_key = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

with open("config.json", "w+") as f:
    config = {}
    config["local_db_user"] = input("Input user name of local database(default 'root'): ") or "root"
    config["local_db_name"] = input("Input database name of local database(default 'database'): ") or "database"
    config["local_db_password"] = input("Input password name of local database: ")
    config["local_db_port"] = input("Input port of local database(default 3306): ") or "3306"
    config["DJANGO_SECRET_KEY"] = secret_key

    f.write(json.dumps(config, indent=4))

with open("zappa_settings.json", "r+", encoding='utf-8') as f:
    zappa_settings = json.load(f) or {}

    zappa_stage_name = input("Input zappa stage name(default dev): ") or "dev"
    if zappa_stage_name not in zappa_settings:
        raise ValueError(f"Given zappa stage name({zappa_stage_name}) is not found!")

    config = {}
    config["prod_db_endpoint"] = input("Input endpoint of production database: ")
    config["prod_db_user"] = input("Input user name of production database: ")
    config["prod_db_name"] = input("Input database name of production database: ")
    config["prod_db_password"] = input("Input password name of production database: ")
    config["prod_db_port"] = input("Input port of production database(default 3306): ") or "3306"

    use_cloudfront = input("Do you use cloudfront for static files? (default 'n') [y/n]: ") or "n"

    if use_cloudfront == "y":
        config["cloudfront_url"] = input("Input cloudfront url: ").replace("https://", "").replace("http://", "")
    else:
        config["s3_bucket"] = input("Input s3 bucket name of static files: ")

    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    config["AWS_ACCESS_KEY_ID"] = credentials.access_key
    config["AWS_SECRET_ACCESS_KEY"] = credentials.secret_key
    config["AWS_REGION"] = session.region_name
    config["DJANGO_SECRET_KEY"] = secret_key
    zappa_settings[zappa_stage_name]["environment_variables"] = config
    zappa_settings[zappa_stage_name]["keep_warm"] = False

    is_set_vpc_config = input("You want to set vpc config? (default 'n') [y/n]")

    if is_set_vpc_config.lower() == "y":
        vpc_config = {}
        vpc_config["SubnetIds"] = input("Input subnet ids(separator is comma[,]): ").split(",")
        vpc_config["SecurityGroupIds"] = input("Input security group ids(separator is comma[,]): ").split(",")

        zappa_settings[zappa_stage_name]["vpc_config"] = vpc_config

    result = json.dumps(zappa_settings, indent=4)
    print(result)
    is_okay = input("Does this look okay? (default 'y') [y/n]: ") or 'y'

    f.seek(0)
    if is_okay.lower() == "y":
        f.write(result)
        print("Done! Run zappa deploy.")
    else:
        print("Sorry to hear that! Please run setup.py again.")
