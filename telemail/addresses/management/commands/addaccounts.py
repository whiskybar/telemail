import sys
import getpass
from django.core.management.base import BaseCommand
from telemail.addresses.models import Account


class Command(BaseCommand):
    help = 'Adds one or more accounts (users).'


    def process_line(self, address):
        try:
            address, password = address.split(':', 1)
        except ValueError:
            password = getpass.getpass('Enter password for the address "%s": ' % address)
        account, created = Account.objects.get_or_create(address=address)
        account.password = password
        account.save()

    def handle(self, *args, **options):
        process_stdin = False
        if args:
            for arg in args:
                if arg == '-':
                    process_stdin = True
                else:
                   self.process_line(arg)
        else:
            process_stdin = True
        if process_stdin:
            for line in sys.stdin:
                 self.process_line(line.strip())
