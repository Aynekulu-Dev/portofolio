"""
Django settings for DevPortfolio Pro project.
"""

import os
import sys
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================== SECURITY ====================
SECRET_KEY = config('SECRET_KEY', default='django-insecure-development-key-change-this-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Get ALLOWED_HOSTS from environment variable
ALLOWED_HOSTS_STR = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_STR.split(',') if host.strip()]

# Add 'testserver' for testing
if 'test' in sys.argv:
    ALLOWED_HOSTS.append('testserver')

# ==================== APPLICATION DEFINITION ====================
INSTALLED_APPS = [
    # Django Core Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    
    # Third-party Apps
    'crispy_forms',
    'crispy_tailwind',
    'tinymce',
    'taggit',
    # 'storages',  # Uncomment when using AWS S3
    
    # Local Apps
    'core',
    'portfolio',
    'blog',
    'skills',
    'contact',
    'utils',  # Keep only if you need it
]

# ==================== MIDDLEWARE ====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==================== URL & TEMPLATE CONFIGURATION ====================
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',  # Custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ==================== DATABASE CONFIGURATION ====================
# Development database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override with PostgreSQL if in production or specified
if not DEBUG or config('USE_POSTGRESQL', default=False, cast=bool):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='devportfolio_db'),
            'USER': config('DB_USER', default='devportfolio_user'),
            'PASSWORD': config('DB_PASSWORD', default=''),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

# ==================== PASSWORD VALIDATION ====================
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

# ==================== INTERNATIONALIZATION ====================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==================== STATIC & MEDIA FILES ====================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = []  # Empty - we use STATIC_ROOT for production

# WhiteNoise configuration for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== THIRD-PARTY CONFIGURATION ====================
# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': '100%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
        textcolor save link image media preview codesample contextmenu
        table code lists fullscreen insertdatetime nonbreaking
        contextmenu directionality searchreplace wordcount visualblocks
        visualchars code fullscreen autolink lists charmap print hr
        anchor pagebreak
    ''',
    'toolbar1': '''
        fullscreen preview bold italic underline | fontselect,
        fontsizeselect | forecolor backcolor | alignleft alignright |
        aligncenter alignjustify | indent outdent | bullist numlist table |
        | link image media | codesample |
    ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# Taggit
TAGGIT_CASE_INSENSITIVE = True

# Site ID (for flatpages, sitemaps, etc.)
SITE_ID = config('SITE_ID', default=1, cast=int)

# ==================== EMAIL CONFIGURATION ====================
if DEBUG:
    # Development: Print emails to console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Production: Use SMTP
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
    EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
    DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER', default='noreply@yourdomain.com')
    SERVER_EMAIL = config('EMAIL_HOST_USER', default='noreply@yourdomain.com')

# ==================== SECURITY SETTINGS FOR PRODUCTION ====================
if not DEBUG:
    # Security headers
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # SSL/HTTPS settings (uncomment when you have SSL)
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    
    # HSTS settings (uncomment when you have SSL)
    # SECURE_HSTS_SECONDS = 31536000  # 1 year
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True
    
    # Logging configuration
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR / 'logs/django_error.log',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

# ==================== CUSTOM SETTINGS ====================
# Contact email for the contact form
CONTACT_EMAIL = config('EMAIL_HOST_USER', default='')

# AWS Settings (for future S3 integration)
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='eu-west-1')

# Uncomment to use S3 for media files
# if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME:
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     AWS_S3_FILE_OVERWRITE = False
#     AWS_DEFAULT_ACL = 'private'
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

# ==================== ENVIRONMENT DETECTION ====================
# Print environment info
if DEBUG:
    print(f"✅ Running in DEVELOPMENT mode")
    print(f"📁 Database: {DATABASES['default']['ENGINE']}")
    print(f"🌐 Allowed Hosts: {ALLOWED_HOSTS}")
else:
    print(f"🚀 Running in PRODUCTION mode")
    print(f"📁 Database: {DATABASES['default']['ENGINE']}")
    print(f"🌐 Allowed Hosts: {ALLOWED_HOSTS}")