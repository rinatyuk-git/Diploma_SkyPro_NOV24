from config import settings
from django.db import models
NULLABLE = {"blank": True, "null": True}


class Document(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="Specify Owner",
        **NULLABLE,
    )  # User — Owner of doc
    is_approved = models.BooleanField(
        verbose_name='Document confirmation sign',
        **NULLABLE,
    )  # Approval sign
    name = models.CharField(
        verbose_name="Document Name",
        help_text="Specify Document Name",
    )  # Name of doc
