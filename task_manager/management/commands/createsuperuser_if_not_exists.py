import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dotenv import load_dotenv


load_dotenv()


class Command(BaseCommand):
    """
    Create a superuser if not exists
    Example:
        manage.py createsuperuser_if_not_exists
    """
    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')

        user = get_user_model()
        if user.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS('User already exists!'))
            return

        user.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully created superuser')
        )
