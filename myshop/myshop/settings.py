from decouple import config

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = 'django-insecure-(j=w=h2su#fu@)!zed5a4ww*s%k!&wla+!clp5xub7=ubog=1m'
# DEBUG = True

SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True


#Телеграм pip install python-telegram-bot
TELEGRAM_BOT_TOKEN=config('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID=config('TELEGRAM_CHAT_ID')


if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'magazine.pythonanywhere.com',
]

CSRF_TRUSTED_ORIGINS = [
    "https://magazine.pythonanywhere.com",
]

#Оплата pip install liqpay-python
LIQPAY_PUBLIC_KEY = config('LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = config('LIQPAY_PRIVATE_KEY')




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'shop.apps.ShopConfig',#приложенеие
    'cart.apps.CartConfig', #Приложение корзины 
    'orders.apps.OrdersConfig', #Приложение заказов
    'review.apps.ReviewConfig', #Приложение отзывов
    'accounts.apps.AccountsConfig', #Приложение аккаунтов
 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # работа с сессиями
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart', #добавить в settings.py в раздел TEMPLATES 'cart.context_processors.cart',
           
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'




# базаданных SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# базаданных Postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST', default='127.0.0.1'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }






AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Это ключ, который будет использоваться для хранения корзины в поль- зовательском сеансе
CART_SESSION_ID = 'cart'

# Авторизация myshop/review
AUTH_USER_MODEL = 'auth.User'
#  после авторизации перенаправляет на главную страницу
LOGIN_REDIRECT_URL = '/'
#  после выхода перенаправляет на главную страницу
LOGOUT_REDIRECT_URL = '/'
