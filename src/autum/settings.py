import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '@0^4x*p73s#e4lc@1+t%y1osn*nbjw3x$z^v(h0hp6icy+a&t('
DEBUG = True

ALLOWED_HOSTS = []
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER='megha.gajbhiye.test@gmail.com'
EMAIL_HOST_PASSWORD='Tester@123'
EMAIL_PORT = 587
EMAIL_USE_TLS= True

INSTALLED_APPS = (
    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third Party Apps
    'crispy_forms',
    'registration',
    #'djdatadog',
    #My Apps
    'cloud',
    'aws',
    'azure1',
    'rackspace',
    'google',
    'oracle',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'autum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'autum.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static_in_pro/our_static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env","static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_in_pro","our_static"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env","media_root")


#Crispy form tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'


#Django-Registration-Redux Settings 
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
