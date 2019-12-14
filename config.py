import secrets
import os

ADMIN_EMAIL_ADDRESS = os.environ.get('APP_ADMIN_EMAIL', None)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ.get('APP_SECRET_KEY', secrets.token_urlsafe())
SQLALCHEMY_DATABASE_URI = os.environ.get('APP_DB_URL', 
                        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app.db')))
SQLALCHEMY_TRACK_MODIFICATIONS = False
