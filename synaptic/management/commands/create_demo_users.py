from django.core.management.base import BaseCommand
from synaptic.models import User
from .demo_users import DEMO_USERS


user_objects = []

class Command(BaseCommand):
    help = 'Creates generic demo users in the database.'

    def handle(self, *args, **options):
        for user in DEMO_USERS:
            user_objects.append(User(**user))
        try:
            User.objects.bulk_create(user_objects)
            self.stdout.write(self.style.SUCCESS('Successfully created demo users in the database.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred creating the users: {str(e)}'))

