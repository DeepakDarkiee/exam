from .base import *

DEBUG = True

ALLOWED_HOSTS = ['exam.djangobabu.com']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "exam_db",
        "USER": "djangobabu",
        "PASSWORD": "djangobabu",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://188568e514ec4fbaa4e3be4a8ecf7974@o578639.ingest.sentry.io/6020670",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)