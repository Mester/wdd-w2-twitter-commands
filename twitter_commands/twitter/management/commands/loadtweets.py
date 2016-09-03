from django.core.management.base import BaseCommand, CommandError
from twitter.models import User, Tweet
from django.conf import settings
import tweepy


class Command(BaseCommand):
    help = "loadtweetsss command"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('username', help='The user whose tweets to get.')

        # Named (optional) arguments
        parser.add_argument(
            '--count',
            default=200,
            help='How many tweets to import, max 200.',
        )

    def handle(self, *args, **options):
        if not User.objects.filter(username=options['username']):
            raise CommandError('User "{}" does not exist'.format(options['username']))

        auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        access_token = '701785233641893888-kw0qIs1nfieUqpyxfZteLrZcrO9uDt6'
        access_token_secret = '3Fuxox2nw87MAWJgECzPduFkux57iq02LTGuIvGjIMN7U'
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

            # print(args)
            # print(options)
