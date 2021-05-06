import os

class Config:
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ###

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass

    #SQLALCHEMY_DATABASE_URI = 'postgresql://dolmsujsgcpwth:8a60dac1d0c074445614c8a4c6a3019d50e180e48f07600c204cee12962876c0@ec2-184-72-236-3.compute-1.amazonaws.com:5432/dfkm6g7o8i8v2u'
    #SQLALCHEMY_DATABASE_URI='postgresql://cldhnjtxxhymfa:03575ce94d6db2282ae6a842942a8e34660f538fa5e5b05ecc8a3f48e29fb8ad@ec2-23-23-128-222.compute-1.amazonaws.com:5432/dbeme2dn5uq3kd'
    
    #postgres://cldhnjtxxhymfa:03575ce94d6db2282ae6a842942a8e34660f538fa5e5b05ecc8a3f48e29fb8ad@ec2-23-23-128-222.compute-1.amazonaws.com:5432/dbeme2dn5uq3kd


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Ivonne1236987@localhost:5432/zed'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}