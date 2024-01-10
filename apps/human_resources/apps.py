from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["HumanResourcesConfig"]


class HumanResourcesConfig(apps.AppConfig):
    """Represents the `human_resources` app and its configuration."""

    name = "human_resources"
    verbose_name = _("Human Resources")
