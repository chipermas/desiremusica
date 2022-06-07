class Config(object):
    SECRET_KEY = 'Lonchex'    
    
class DevelopmentConfig(Config):
    DEBUG = True    
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/tesisdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
