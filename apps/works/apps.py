from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["WorksConfig"]


class WorksConfig(apps.AppConfig):
    """Represents the `works` app and its configuration."""

    name = "works"
    verbose_name = _("Works")
