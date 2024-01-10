from django.db import models

__all__ = ["Model"]


class Model(models.Model):
    """Represents a base for defining models in the project's apps."""

    class Meta:
        abstract = True
