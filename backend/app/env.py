import os

APP_ENV=os.environ.get("APP_ENV")

DB_USER = os.environ.get("MYSQL_USER")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("MYSQL_DATABASE")

ROOT = os.environ.get("ROOT")
ORIGINS = os.environ.get("ORIGINS").split(",")

HOST = os.environ.get("HOST")
GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

SALT = os.environ.get("SALT")