import os

class Config:
    """
    """

    SECRET_KEY = '1131'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:12345@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'aliimohamud185@gmail.com'
    MAIL_PASSWORD = '0746881243A'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
class DevConfig(Config):
    """
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:12345@localhost/pitch'
    DEBUG = True    

config_options = {
'development':DevConfig,
'production':ProdConfig
}    