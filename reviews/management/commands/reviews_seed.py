import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from notifications import models as noti_model


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        posts = noti_model.Posting.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "post": lambda x: random.choice(posts),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
