import os
import sys
import logging
from .settings import INSTALLED_APPS, MIDDLEWARE_CLASSES


DEBUG = True
USE_HANDLER = True
INTERNAL_IPS = (
    '127.0.0.1'
)


INSTALLED_APPS += (
    'django_extensions',
)

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'EXCEPTION_HANDLER': 'core.exceptions.status_exception_handler',
#     'TEST_EXCEPTION_HANDLER': 'core.exceptions.status_exception_handler',
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     ),
#     'DEFAULT_PAGINATION_SERIALIZER_CLASS':
#         'core.pagination.CorePaginationSerializer',
#     'DEFAULT_FILTER_BACKENDS': ()
#
# }
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '\033[0;31m%(levelname)s %(name)s\033[0;33m %(asctime)s\033[0;37m '
                      '%(message)s'
        },
        'simple': {
            'format': '\033[0;31m%(levelname)s \033[1;33m%(name)s\033[0;37m %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        # 'essays.essays_process': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
        'essays': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },

        'events': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'emails': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'manage': {
            'handlers': [],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends':{
            'handlers': [],
            'level': 'DEBUG',
            'propagate': False,
        }

    },
}


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kundendienstgv'
EMAIL_HOST_PASSWORD = 'Av1dr0ck5!'
EMAIL_PORT = 587

# if DEBUG:
#     INTERNAL_IPS = ('127.0.0.1',)
#     MIDDLEWARE_CLASSES += (
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     )
#
#     INSTALLED_APPS += (
#         'debug_toolbar',
#     )
#
#     DEBUG_TOOLBAR_PANELS = (
#         'debug_toolbar.panels.version.VersionDebugPanel',
#         'debug_toolbar.panels.timer.TimerDebugPanel',
#         # 'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#         'debug_toolbar.panels.headers.HeaderDebugPanel',
#         #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
#         'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#         'debug_toolbar.panels.sql.SQLDebugPanel',
#         'debug_toolbar.panels.template.TemplateDebugPanel',
#         'debug_toolbar.panels.cache.CacheDebugPanel',
#         'debug_toolbar.panels.signals.SignalDebugPanel',
#         # 'debug_toolbar.panels.logger.LoggingPanel',
#     )
#
#     DEBUG_TOOLBAR_CONFIG = {
#         'INTERCEPT_REDIRECTS': False,
#     }