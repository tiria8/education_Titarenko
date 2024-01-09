import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            user_email=os.environ.get('SUPER_USER_EMAIL'),
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(os.environ.get('SUPER_USER_PASSWORD'))
        user.save()
