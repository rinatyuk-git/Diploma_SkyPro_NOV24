from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Creation of ModeratorUser """
    def handle(self, *args, **options):
        user = User.objects.create(email="moderator@mail.com")
        user.set_password("Moder1_1redoM")
        user.is_active = True
        user.is_staff = True
        user.save()
