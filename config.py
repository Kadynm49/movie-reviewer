import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'w346e5dyrftugih7yt68r5dctufgvh'