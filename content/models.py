from config import settings
from django.db import models
NULLABLE = {"blank": True, "null": True}


STATUS_CHOICES = {
    "a": "Approved",
    "d": "Declined",
}


class Document(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Owner",
        help_text="Specify Owner",
        **NULLABLE,
    )  # User — Owner of doc
    status = models.CharField(
        max_length=1,
        verbose_name='Document approving mark',
        choices=STATUS_CHOICES,
        **NULLABLE,
    )  # Approval sign
    name = models.CharField(
        verbose_name="Document Name",
        help_text="Specify Document Name",
    )  # Name of doc

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
