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
            default=10,
            type=int,
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

        user = User.objects.get(username=options['username'])
        count = 0
        for status in tweepy.Cursor(api.user_timeline, id=options['username']).items(options['count']):
            tweet, created = Tweet.objects.get_or_create(user=user, content=status.text, created=status.created_at)
            if created:
                tweet.created = status.created_at
                tweet.save()
                count += 1

        self.stdout.write(self.style.SUCCESS('Finished. {} tweets have been imported.'.format(count)))
