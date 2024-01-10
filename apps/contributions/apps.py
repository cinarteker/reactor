from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["ContributionsConfig"]


class ContributionsConfig(apps.AppConfig):
    """Represents the `contributions` app and its configuration."""

    name = "contributions"
    verbose_name = _("Contributions")
