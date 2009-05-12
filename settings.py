# -*- coding: utf-8 -*-
from ragendja.settings_pre import *

# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Wuf1nXQZ6yor5TxF0QKhm5vwnsZAXnqa'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = False
#LANGUAGE_CODE = 'en'

#Restrict supported languages (and JS media generation)
#LANGUAGES = (
#    ('de', 'German'),
#    ('en', 'English'),
#)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    #'django.core.context_processors.i18n',
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware',
    # Django authentication
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Google authentication
    #'ragendja.auth.middleware.GoogleAuthenticationMiddleware',
    # Hybrid Django/Google authentication
    #'ragendja.auth.middleware.HybridAuthenticationMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

# Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.google_models'
#AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
# Hybrid Django/Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

GLOBALTAGS = (
    #'ragendja.templatetags.ragendjatags',
    #'django.templatetags.i18n',
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.sessions',
    'appenginepatcher',
    'app',
)

# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
    # Example:
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'yetanotherapp',
)

TIME_FORMAT = "H:i"

from ragendja.settings_post import *
