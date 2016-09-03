from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "loadtweetsss command"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username', help='The user whose tweets to get')

        # Named (optional) arguments
        parser.add_argument(
            '--count',
            default=200,
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        print(args)
        print(options)
