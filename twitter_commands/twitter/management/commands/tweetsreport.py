from django.core.management.base import BaseCommand, CommandError
from twitter.models import Tweet, User
from datetime import datetime
import argparse
from django.core.mail import send_mail


# def string_to_datetime(string):
#     return datetime.strptime(string, '%Y-%m-%d')

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'".format(s)
        raise argparse.ArgumentTypeError(msg)


class Command(BaseCommand):
    help = "tweetsreporttt command"

    def add_arguments(self, parser):
        # Positional arguments
        
        # Named (optional) arguments
        parser.add_argument(
            '--from_date',
            type=valid_date,
            # default=datetime.fromtimestamp(0),
            help='Starting date to get tweets from',
        )
        parser.add_argument(
            '--to_date',
            type=valid_date,
            # default=datetime.now(),
            help='End date to get tweets from',
        )

    def handle(self, *args, **options):
        user_counts_tuples = []
        for user in User.objects.all():
            tweets = Tweet.objects.filter(user=user)
            if 'from_date' in options and options['from_date']:
                tweets = tweets.filter(created__gte=options['from_date'])
            if 'to_date' in options and options['to_date']:
                tweets = tweets.filter(created__lte=options['to_date'])
            user_counts_tuples.append((user, tweets.count()))
        message = ""
        for user, count in user_counts_tuples:
            message += "{}: {}".format(user.username, count)
        send_mail('tweets report',
                  message,
                  'tweets@reports.r.us',
                  ['who@knows.com', ])
