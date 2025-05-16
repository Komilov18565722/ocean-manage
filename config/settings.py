from datetime import timedelta
from pathlib import Path
from environs import Env
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
env.read_env()
SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")
# DEBUG=True

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = list(map(str, env.str("CORS_ALLOWED_ORIGINS").split(' ')))

ALLOWED_HOSTS = list(map(str, env.str("ALLOWED_HOSTS").split(' ')))
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True


CSRF_TRUSTED_ORIGINS = [
    "http://192.168.23.144:8000"
]

APPEND_SLASH = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "storages",

    # Local apps
    'accounts',
    'transaction',

    # Out apps
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "django_filters",

]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60*24),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(weeks=1),
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "accounts.middleware.StateCheckMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = "accounts.User"

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [("redis", REDIS_PORT)],
#         },
#     },
# }



AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# MEDIA_URL = "media/"
# MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# MEDIA_URL = "media/"
# MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
PASSWORD_RESET_TIMEOUT = 259200
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "selfstudystartup@gmail.com"
# EMAIL_HOST_PASSWORD = "wambfmqmnshycpos"

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

# AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL")
#

# AWS_QUERYSTRING_AUTH = False
# AWS_LOCATION = 'media'
# AWS_DEFAULT_ACL = 'public-read'
# MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}/'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#
# from .utils import S3Uploader
# uploader = S3Uploader(
#     bucket_name=AWS_STORAGE_BUCKET_NAME,
#     endpoint_url="https://s3.twcstorage.ru",
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
# )
#
# PAYPAL_CLIENT_ID = "AUofBM6InQNJWzMBfHR-71y6j_q59gqDWJ3C_uxVxYKwp_OwljMM6raEv8-BoxECGI6gHg4KO2rINZRr"
# PAYPAL_SECRET = "EA_-mgJjjagdtvpIPwRzxrfKhYBRa6CZWzctbzfRTHI7z2sM9yyOo04Kpv-K4Ch73czwpHuScS2N-n-_"
# PAYPAL_MODE = "sandbox"

# log_dir = os.path.join(BASE_DIR, "logs")
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": True,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "simple",
#         },
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "filename": os.path.join(BASE_DIR / "logs", "app.log"),
#             "when": "midnight",  
#             "interval": 1,       
#             "backupCount": 70,    # Keep logs for the last 7 days
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["file"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "django.request": {
#             "handlers": ["file", "console"],
#             "level": "WARNING",
#             "propagate": False,
#         }
#     },
# }
