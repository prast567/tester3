import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = "techconfsrv.postgres.database.azure.com"
    POSTGRES_USER = "tc_admin@techconfsrv"
    POSTGRES_PW = "Orange@789"
    POSTGRES_DB = "techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL,
                                                          db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://techconf.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=yUN5LyhL1xYu1/KWQln2Ivm+2umRWboHzQzy189TlFU='
    SERVICE_BUS_QUEUE_NAME = 'notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'raj15850@gmail.com'
    SENDGRID_API_KEY = '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"'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
