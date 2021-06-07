from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter():
            User.objects.create_superuser("admin", "admin@a.a", "admin")
