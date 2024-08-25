import os
import certifi

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
os.environ['SSL_CERT_FILE'] = certifi.where()

SECRET_KEY = "mp5"

# reCAPTCHA keys
RECAPTCHA_PUBLIC_KEY = '6Le8j5cpAAAAANRASvj1p1NzU7w8KLJw9RYm6kxk'# 공인키
RECAPTCHA_PRIVATE_KEY = '6Le8j5cpAAAAANRASvj1p1NzU7w8KLJw9RYm6kxk'#비밀키