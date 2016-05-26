"""
Django settings for societe project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Stripe Test Key's

# Braintree API Keys
BRAINTREE_MERCHANT_ID = '<your_merchant_id>'
BRAINTREE_PUBLIC_KEY = '<your_public_key>'
BRAINTREE_PRIVATE_KEY = '<your_private_key>'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-%*5#5wtg9#128lvye-ln8^-s6__3&&*jm-_s)&h_2hj61fs_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Project app
    'landing_page',
    'contact',
    'reviews',
    # instaled third party app
    'analytical',
    'axes',
    'autocomplete_light',
    'bootstrap3',
    'datetimewidget',
    'django_countries',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.google',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
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
    # django-axes MIDDLEWARE_CLASSES
    'axes.middleware.FailedLoginMiddleware',
)

ROOT_URLCONF = 'societe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'societe.wsgi.application'

# This also use allauth
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Writing configuration for Heroku deployment
# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# loading local_settings.py
try:
    from .local_settings import *
except Exception as e:
    pass

# import config.py from django_social_app
from .config import *

# allauth configuration

# Specific the adapter class to use, allowing you to alter certain default behaviour
# ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

# Specific the login method to use
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = "username", "email", "username_email"

# Determines whether or not an e-mail address is automatically confirmed by a mere GET request
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = settings.LOGIN_URL

# The URL to redirect to after a successful e-mail confirmation, in case of an authenticated user.
# Set to None to use settings.LOGIN_REDIRECT_URL.
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

# Determines the expiration date of email confirmation mails (# of days).
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

# The user is required to hand over an e-mail address when signing up.
# ACCOUNT_EMAIL_REQUIRED = False

# Determines the e-mail verification method during signup – choose one of “mandatory”, “optional”, or “none”.
# When set to “mandatory” the user is blocked from logging in until the email address is verified.
# Choose “optional” or “none” to allow logins with an unverified e-mail address.
# In case of “optional”, the e-mail verification mail is still sent,
# whereas in case of “none” no e-mail verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "none"

# Subject-line prefix to use for email messages sent.
# By default, the name of the current Site (django.contrib.sites) is used.
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Site]"

# The default protocol used for when generating URLs, e.g. for the password forgotten procedure.
# Note that this is a default only – see the section on HTTPS for more information.
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# Used to override forms, for example: {‘login’: ‘myapp.forms.LoginForm’}
# ACCOUNT_FORMS = {}

# Determines whether or not the user is automatically logged out by a mere GET request.
# See documentation for the LogoutView for details.
ACCOUNT_LOGOUT_ON_GET = False

# Determines whether or not the user is automatically logged out after changing or setting their password.
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

# The URL (or URL name) to return to after the user logs out.
# This is the counterpart to Django’s LOGIN_REDIRECT_URL.
# ACCOUNT_LOGOUT_REDIRECT_URL = "/account/logout"

# A string pointing to a custom form class (e.g. ‘myapp.forms.SignupForm’) that is used during signup
# to ask the user for additional input (e.g. newsletter signup, birth date). This class should implement
# a def signup(self, request, user) method, where user represents the newly signed up user.
# ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in their password twice to avoid typo’s.
# ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses
# ACCOUNT_UNIQUE_EMAIL = True

# The name of the field containing the username, if any. See custom user models.
# ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

# The name of the field containing the email, if any. See custom user models.
# ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

# A callable (or string of the form ‘some.module.callable_name’) that takes a user as its only argument
# and returns the display name of the user. The default implementation returns user.username.
# ACCOUNT_USER_DISPLAY = a callable returning user.username

# An integer specifying the minimum allowed length of a username.
# ACCOUNT_USERNAME_MIN_LENGTH = 1

# A list of usernames that can’t be used by user.
# ACCOUNT_USERNAME_BLACKLIST = []

# The user is required to enter a username when signing up. Note that the user will be asked to do so
# even if ACCOUNT_AUTHENTICATION_METHOD is set to email. Set to False when you do not
# wish to prompt the user to enter a username.
# ACCOUNT_USERNAME_REQUIRED = True

# render_value parameter as passed to PasswordInput fields.
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# An integer specifying the minimum password length.
# ACCOUNT_PASSWORD_MIN_LENGTH = 6

# The default behaviour is not log users in and to redirect them to
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL.
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# By changing this setting to True, users will automatically be logged in once they have reset their
# password. By default they are redirected to the password reset done page.
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = False

# Controls the life time of the session. Set to None to ask the user (“Remember me?”), False to not
# remember, and True to always remember.
# ACCOUNT_SESSION_REMEMBER = None

# How long before the session cookie expires in seconds. Defaults to 1814400 seconds, or 3 weeks.
# ACCOUNT_SESSION_COOKIE_AGE = 1814400

# The default behaviour is to redirect authenticated users to ACCOUNT_LOGIN_REDIRECT_URL
# when they try accessing login/signup pages.
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

# Specifies the adapter class to use, allowing you to alter certain default behaviour.
# SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"

# Request e-mail address from 3rd import party account provider?
# E.g. using OpenID AX, or the Facebook “email” permission.
SOCIALACCOUNT_QUERY_EMAIL = True

# Attempt to bypass the signup form by using fields (e.g. username, email) retrieved from the import social
# account provider. If a conflict arises due to a duplicate e-mail address the signup form will still kick in.
# SOCIALACCOUNT_AUTO_SIGNUP = True

# The user is required to hand over an e-mail address when signing up using a social account.
# SOCIALACCOUNT_EMAIL_REQUIRED (=ACCOUNT_EMAIL_REQUIRED)

# As ACCOUNT_EMAIL_VERIFICATION, but for social accounts.
# SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION

# Used to override forms, for example: {‘signup’: ‘myapp.forms.SignupForm’}
# SOCIALACCOUNT_FORMS = {}

# Dictionary containing provider specific settings.
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        # we use facebook js_sdk instead od oauth2
        'METHOD': 'js_sdk',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        # using AUTH_PARAMS to pass along other parametees
        # to the FB.login JS SDK call
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        # field are fetch from the import Graph API
        'FIELDS': ['first_name', 'last_name', 'email', 'birthday'],
        # JS SDK return a short-lived token suitable for client-side use.
        'EXCHANGE_TOKEN': True,
        # Chose the current active language of the request
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        # Facebook Graph API version
        'VERSION': 'v2.5'
    },
    'linkedin': {
        'SCOPE': ['r_emailaddress'],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'public-profile-url'
        ]
    }
}

# Indicates whether or not the access tokens are stored in the database.
# SOCIALACCOUNT_STORE_TOKENS = True

# login redirect url
LOGIN_REDIRECT_URL = "/contact"

# MEMCACHE Configuration for Heroku
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CAHCES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiriation
        # timeout that should be applied to keys! Setting it to 'None'
        # disables expiration.
        'TIMEOUT': None,

        'OPTIONS': {
            # Enable faster IO
            'no_block': True,
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout for set/get requests
            '_pool_timeout': 2000,

            # Use consistent hashing for failover
            'ketama': True,

            # Configure failover timings
            'connect_timeout': 2000,
            'remove_failed': 4,
            'retry_timeout': 2,
            'dead_timeout': 10
        }
    }
}

# Default settings
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': 'https://code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': '',

    # Field class to use in horizontal forms
    'horizontal_field_class': '',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set HTML disabled attribute on disabled fields
    'set_disabled': False,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers': {
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

# Customizing Axes

# Number of login attempts allowed before a record is created for the failed logins.
AXES_LOGIN_FAILURE_LIMIT = 3

# After the number os allowed login attempts are exceeded, should we lock this IP (and optinal user agend)?
AXES_LOCK_OUT_AT_FAILURE = True

# If True, lock out / log based on an IP address AND a user agent. This means requests from different import user
# agents but from the import same IP are treated differently.
AXES_USE_USER_AGENT = True

# Defines a period of inactivity after which old failed login attempts will be forgotten. You can set to a
# python timedelta object or an integer, if you set it to be integer it will represent a number of hours
AXES_COOLOFF_TIME = 50

# Specifies a logging mechanism for axes to use
AXES_LOCKOUT_TEMPLATE = 'axes.watch_login'

# Specifies a template to render when a user is locked out. Template receives cooloff_time and failure_limit as
# context variables
AXES_LOCKOUT_TEMPLATE = None

# Specifies a URL to redirect to on lockout. If both AXES_LOCKOUT_TEMPLATE and AXES_LOCKOUT_URL are set, the template
# will be used
AXES_LOCKOUT_URL = None

# If Truem you'll see slightly more logging for Axes
AXES_VERBOSE = True

# The name of the for field that contains your usernames
# AXES_USERNAME_FORM_FIELD = username

# If True prevents to login from IP import under particular user if attempts limit exceed, otherwise lock out based on
# IP. Default: False
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = False

# Clicky configuration
CLICKY_SITE_ID = '100938376'

# Google analytics configuration
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-75841576-1'

# Display advertising got Google analytics
GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = True

# Tracking site speed on Google analytics
GOOGLE_ANALYTICS_SITE_SPEED = True
