import secrets
import os

SECRET_KEY = os.environ.get('APP_SECRET_KEY', secrets.token_urlsafe())
    
