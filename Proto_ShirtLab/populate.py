import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Proto_ShirtLab.settings')

import django
django.setup()

from faker import Faker
from app_proto.models import SLUser

fkgn = Faker()

def populate(n=5):

    for x in range(n):
        fk_name = fkgn.name().split()
        fk_first = fk_name[0]
        fk_last = fk_name[1]
        fk_email = fkgn.email()

        user = SLUser.objects.get_or_create(first_name=fk_first,
                                            last_name=fk_last,
                                            email=fk_email)[0]

print('Start populating')
populate(10)
print('Populating finished')
