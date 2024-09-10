import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/sys'
    SQLALCHEMY_TRACK_MODIFICATIONS = False