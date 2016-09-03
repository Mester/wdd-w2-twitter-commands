from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "tweetsreporttt command"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username')

        # Named (optional) arguments
        # parser.add_argument(
        #     '--delete',
        #     action='store_true',
        #     dest='delete',
        #     default=False,
        #     help='Delete poll instead of closing it',
        # )

    def handle(self, *args, **options):
        print(args)
        print(options)
