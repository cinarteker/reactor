from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["UnitsConfig"]


class UnitsConfig(apps.AppConfig):
    """Represents the `units` app and its configuration."""

    name = "units"
    verbose_name = _("Units")
