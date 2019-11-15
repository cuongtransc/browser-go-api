import os
# local db
# ! Environment Variable
# DATABASE = 'postgresql://localhost/browser-go'
DATABASE = 'postgresql://dev:dev123@172.17.0.1/god_of_go'

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE
    PORT = 5000


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://mzwaocmnwvesac:d86d256a9e73639d0ac1eba3651f3f5268540e6417b110265fd58398358d1c1b@ec2-174-129-227-51.compute-1.amazonaws.com:5432/d1jbr1uiojpma'
