from django.core.management.base import BaseCommand
from quiz.synaptic.models import User
from quiz.demo_quiz import demo_users


user_objects = []

class Command(BaseCommand):
    help = 'Creates generic demo users in the database.'

    def handle(self, *args, **options):
        for user in demo_users.DEMO_USERS:
            user_objects.append(User(**user))
        User.objects.bulk_create(user_objects)
        self.stdout.write(self.style.SUCCESS('Successfully created demo users in the database.'))