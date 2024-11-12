from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from content.models import Document, STATUS_CHOICES
from users.models import User


def doc_created_message(mailing_item: Document):
    """ Подготовка рассылки писем """
    send_mail(
        f'Doc {mailing_item.name} created',
        f'Doc {mailing_item.name} created info',
        EMAIL_HOST_USER,
        [User.objects.filter(is_staff=True, is_superuser=False).first().email],
        fail_silently=False,
    )


@shared_task
def doc_approving_message(instance_id: int):
    """ Подготовка рассылки писем для подтверждения """
    mailing_item = Document.objects.get(id=instance_id)
    subject = f'Doc {mailing_item.name} is {STATUS_CHOICES[mailing_item.status]}'
    message = f'Dear {mailing_item.owner.email}, your doc {mailing_item.name} is {STATUS_CHOICES[mailing_item.status]}'
    email = [mailing_item.owner.email]
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        email,
        fail_silently=False,
    )
