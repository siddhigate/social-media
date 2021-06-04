import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

WTF_CSRD_ENABLED = True

SECRET_KEY = 'hello'

SQLALCHEMY_DATABASE_URI = 'postgres://tejas:123654789@localhost:5432/twitterme'
SQLALCHEMY_TRACK_MODIFICATIONS = True

UPLOAD_FOLDER = 'N:\\Documents\\webdev\\python\\flask-TweetMe\\flaskapp\\static\\profile_pics'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG', 'PNG'])
