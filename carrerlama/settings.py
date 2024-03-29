"""
Django settings for carrerlama project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT   = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8h%b@$t_nq8hp-v1twg#md_je5!(ucih*dmm49n3czg1!x00_g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'social_django',
    'material.theme.indigo',
    'material',
    'material.admin',

    'dashboard.apps.DashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    # 'dashboard',



    'django.contrib.sites',



]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'carrerlama.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'carrerlama.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'carrer_lama',
        'USER': 'root',
        'PASSWORD': 'laptrip0',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}







# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/mediadump/'
MEDIA_SUB_FOLDER_NAME = 'carrer_lama'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'carrer_lama')


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# authentication backend
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)



# Social authentication keys
LOGIN_REDIRECT_URL = "http://139.59.94.59/"
# LOGIN_REDIRECT_URL  = "http://127.0.0.1:8000"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '158282295560-sjaaaiq15pmb2npo2qfrhcau91f6r3jb.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'RFOWoWKiLyEBB6swAHLKLeJj'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False


SOCIAL_AUTH_FACEBOOK_KEY = '145003602901305'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '84a031aa02e53bde3d06472fc37d1bff'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '81dvrduhqhvjgg'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'sNW20A7zjZKn7oU8'

#
# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social_auth.backends.pipeline.social.social_auth_user',
#     'social_auth.backends.pipeline.associate.associate_by_email',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'app.pipeline.redirect_to_form',
#     'app.pipeline.username',
#     'social_auth.backends.pipeline.user.create_user',
#     'social_auth.backends.pipeline.social.associate_user',
#     'social_auth.backends.pipeline.social.load_extra_data',
#     'social_auth.backends.pipeline.user.update_user_details',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'app.pipeline.redirect_to_form2',
#     'app.pipeline.first_name',
# )
