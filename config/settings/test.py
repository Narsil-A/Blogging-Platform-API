"""
With these settings, tests run faster.
"""

from .base import *  # noqa: F403
from .base import TEMPLATES, MIDDLEWARE
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="hpGf4R3O0KgAusKITU2Skkkxy5TIuUn84EbGCEHbtA76ZS2ARqvkqJ75FViOized",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# DEBUGGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore[index]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "http://media.testserver"

# STATIC FILES
# ------------------------------------------------------------------------------
STATIC_ROOT = BASE_DIR / 'staticfiles_test'

# Remove WhiteNoiseMiddleware during tests
MIDDLEWARE = [
    mw for mw in MIDDLEWARE
    if mw != 'whitenoise.middleware.WhiteNoiseMiddleware'
]

# Your stuff...
# ------------------------------------------------------------------------------
