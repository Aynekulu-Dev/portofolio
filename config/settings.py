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
ALLOWED_HOSTS_STR = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,34-250-114-27.nip.io')
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_STR.split(',') if host.strip()]

# Add 'testserver' for testing
if 'test' in sys.argv:
    ALLOWED_HOSTS.append('testserver')

# ==================== APPLICATION DEFINITION ====================
INSTALLED_APPS = [
    # JAZZMIN MUST COME BEFORE django.contrib.admin
    'jazzmin',
    
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

# ==================== JAZZMIN ADMIN CONFIGURATION ====================
JAZZMIN_SETTINGS = {
    # Title on the brand (19 chars max)
    "site_title": "DevPortfolio Admin",
    
    # Title on the login screen (19 chars max)
    "site_header": "DevPortfolio Pro",
    
    # Title on the brand (19 chars max)
    "site_brand": "DevPortfolio",
    
    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "images/admin-logo.png",
    
    # Welcome text on the login screen
    "welcome_sign": "Welcome to DevPortfolio Admin",
    
    # Copyright on the footer
    "copyright": "Aynekulu Molla",
    
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    
    ############
    # Top Menu #
    ############
    
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        
        # External URL that opens in a new window (Permissions can be added)
        {"name": "Live Site", "url": "/", "new_window": True},
        
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"model": "auth.User"},
        
        # Custom admin page link
        {"name": "Analytics", "url": "/admin/analytics/", "permissions": ["auth.view_user"]},
    ],
    
    #############
    # User Menu #
    #############
    
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    
    #############
    # Side Menu #
    #############
    
    # Whether to display the side menu
    "show_sidebar": True,
    
    # Whether to aut expand the menu
    "navigation_expanded": True,
    
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "auth",
        "core",
        "portfolio",
        "blog",
        "skills",
        "contact",
    ],
    
    # Custom icons for side menu apps/models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.SiteSettings": "fas fa-cog",
        "core.Technology": "fas fa-microchip",
        "portfolio.Project": "fas fa-project-diagram",
        "blog.BlogPost": "fas fa-blog",
        "blog.BlogCategory": "fas fa-folder",
        "skills.Skill": "fas fa-code",
        "skills.SkillCategory": "fas fa-layer-group",
        "contact.ContactSubmission": "fas fa-envelope",
    },
    
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,
    
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    
    # Add a language dropdown into the admin
    "language_chooser": False,
}

# Jazzmin UI Tweaks
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}

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
    print(f"🎨 Jazzmin Admin: Enabled")
else:
    print(f"🚀 Running in PRODUCTION mode")
    print(f"📁 Database: {DATABASES['default']['ENGINE']}")
    print(f"🌐 Allowed Hosts: {ALLOWED_HOSTS}")
    print(f"🎨 Jazzmin Admin: Enabled")
# ==================== AUTHENTICATION SETTINGS ====================
LOGOUT_ALLOW_GET = True  # Allow GET requests for logout
LOGOUT_REDIRECT_URL = '/admin/login/'  # Redirect to login after logout
LOGIN_REDIRECT_URL = '/admin/'  # Redirect to admin after login
LOGIN_URL = '/admin/login/'  # URL for login page

# ==================== WHITENOISE SETTINGS ====================
WHITENOISE_ROOT = STATIC_ROOT
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_AUTOREFRESH = True

# Update Jazzmin settings
JAZZMIN_SETTINGS.update({
    "logout_url": "/admin/logout/",
    "login_url": "/admin/login/",
    "login_redirect_url": "/admin/",
})
