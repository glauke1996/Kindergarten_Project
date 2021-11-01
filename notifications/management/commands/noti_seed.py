import random
from django.core.management import BaseCommand
from django_seed import Seed
from users import models as user_model
from notifications import models as noti_model


class Command(BaseCommand):
    help = "This command creates Posting!"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many posts you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_model.User.objects.all()
        seeder.add_entity(
            noti_model.Posting,
            number,
            {"user": lambda x: random.choice(all_users)},
        )
        seeder.execute()
