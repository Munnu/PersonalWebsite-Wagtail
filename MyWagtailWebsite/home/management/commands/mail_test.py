from django.core.mail import send_mail as django_send_mail

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage
from django.core.mail import send_mail as django_send_mail

class Command(BaseCommand):
    help = 'Tests the mailing command'

    def handle(self, *args, **options):
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print "THIS SECTION IS DJANGO_SEND_MAIL SECTION"
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print "INSIDE OF HANDLE"
        # email = EmailMessage('Hello', 'World', to=['moniqueblake4@gmail.com'])
        # email.send()
        django_send_mail("my subject", "my message", "mo@moniqueblake.me", ["moniqueblake4@gmail.com"],
                         fail_silently=False)