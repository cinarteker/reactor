from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["ScienceConfig"]


class ScienceConfig(apps.AppConfig):
    """Represents the `science` app and its configuration."""

    name = "science"
    verbose_name = _("Science")
