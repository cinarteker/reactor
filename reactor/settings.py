from pathlib import Path

import dj_database_url as db_url
from configurations import Configuration
from decouple import config

from django.db import DEFAULT_DB_ALIAS
from django.utils.translation import gettext_lazy as _

__all__ = ["CI", "Development"]

DB_ALIAS_ENVIRONMENT_VARIABLE = "DJANGO_DB_ALIAS"

# Django settings & configurations
# https://docs.djangoproject.com/en/5.0/ref/settings/
# https://django-configurations.readthedocs.io/


class Common(Configuration):
    """Defines settings shared by all the configurations."""

    # Paths

    PROJECT_DIR = Path(__file__).resolve().parent

    BASE_DIR = PROJECT_DIR.parent

    # Databases

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    # Apps & middleware

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        #
        # Project-level apps
        "reactor.core",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    # URLs

    ROOT_URLCONF = "reactor.urls"

    # Template engines

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                PROJECT_DIR / "templates",
            ],
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

    # Internationalization

    USE_I18N = True

    LANGUAGE_CODE = "en"

    LANGUAGES = [
        ("en", _("English")),
        ("pl", _("Polish")),
    ]

    LOCALE_PATHS = [
        PROJECT_DIR / "locale",
    ]

    # Timezone

    USE_TZ = True

    TIME_ZONE = "Europe/Warsaw"

    # Fixtures

    FIXTURE_DIRS = [
        PROJECT_DIR / "fixtures",
    ]

    # Static files

    STATIC_URL = "static/"

    STATICFILES_DIRS = [
        PROJECT_DIR / "static",
    ]

    STATIC_ROOT = BASE_DIR / "assets"

    # Media

    MEDIA_URL = "media/"

    MEDIA_ROOT = BASE_DIR / "media"


class Debugging(Common):
    """Defines a configuration for debugging."""

    # Debugging mode

    DEBUG = True

    # Security

    SECRET_KEY = "django-insecure-secret-key"

    ALLOWED_HOSTS = ["*"]

    @classmethod
    def pre_setup(cls):
        super().pre_setup()

        if DEFAULT_DB_ALIAS not in cls.DATABASES:
            cls.pre_setup_databases()

    @classmethod
    def pre_setup_databases(cls):
        DB_ALIAS = config(DB_ALIAS_ENVIRONMENT_VARIABLE)

        try:
            cls.DATABASES = {DEFAULT_DB_ALIAS: cls.DATABASES[DB_ALIAS]}
        except KeyError as exc_info:
            raise ValueError(
                f"Database with the {DB_ALIAS!r} alias has not been declared for "
                f"the {cls.__name__!r} configuration."
            ) from exc_info


class Development(Debugging):
    """Defines a configuration for development environments."""

    DOTENV = Debugging.BASE_DIR / ".env"

    @classmethod
    def pre_setup_databases(cls):
        cls.DATABASES = {DEFAULT_DB_ALIAS: db_url.config()}


class CI(Debugging):
    """Defines a configuration for CI environments."""

    # Databases

    DATABASES = {
        "sqlite": db_url.parse("sqlite://:memory:"),
    }
