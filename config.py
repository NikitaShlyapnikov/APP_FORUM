import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you_will_never_guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:PS9904516608WSa1$@localhost:5432/app_forum'
    SQLALCHEMY_TRACK_MODIFICATIONS = False