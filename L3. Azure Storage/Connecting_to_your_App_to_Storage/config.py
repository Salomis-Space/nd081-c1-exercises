'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or '[SQL_SERVER_GOES_HERE]'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or '[SQL_DATABASE_GOES_HERE]'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[SQL_USER_NAME_GOES_HERE]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or '[BLOB_ACCOUNT_GOES_HERE]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[BLOB_STORAGE_KEY_GOES_HERE]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or '[BLOB_CONTAINER_GOES_HERE]'
'''
import os

# ---------- Azure SQL Database ----------
SQL_SERVER = os.getenv('SQL_SERVER', 'my-zoo-server.database.windows.net')
SQL_DATABASE = os.getenv('SQL_DATABASE', 'zoodb')
SQL_USER_NAME = os.getenv('SQL_USER_NAME', 'udacity-user')
SQL_PASSWORD = os.getenv('SQL_PASSWORD', 'Uda@12345')
SQL_DRIVER = '{ODBC Driver 17 for SQL Server}'

# ---------- Azure Blob Storage ----------
BLOB_ACCOUNT = os.getenv('BLOB_ACCOUNT', 'zoo1store')
BLOB_STORAGE_KEY = os.getenv('BLOB_STORAGE_KEY', 'EQqq8fBx7VLwVC1Y0UAGMqGhByXFk/77i4KLqE0ORN2VLFIv69OVjhrvYrQkNt60e4LzEujKbZM7+AStQcup1w==')
BLOB_CONTAINER = os.getenv('BLOB_CONTAINER', '$logs')  # Udacity-provided container

# ---------- SQLAlchemy connection string ----------
SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'
