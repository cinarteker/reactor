from django.utils.translation import gettext_lazy as _

from reactor import apps

__all__ = ["PublishingMedia"]


class PublishingMedia(apps.AppConfig):
    """Represents the `publishing_media` app and its configuration."""

    name = "publishing_media"
    verbose_name = _("Publishing Media")
