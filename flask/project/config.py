import os

# could potentially eliminate this if only the secret is needed as it's currently provided in the app factory initiation

class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET")
