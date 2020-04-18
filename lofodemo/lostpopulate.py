import os
os.environ.setdefault('Django_settings_module','lofodemo.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
import random
from random import choice,randint
x=['Adhar Card','Voter Id Card','Passport','Atm Card']
y=['adhar','voterid','passport','atm']
# def add_Card():
#     c=Found.objects.get_or_create(name=random.choice(x))[0]
#     return c

def populate(n):
    faker=Faker()
    for i in range(n):
        lcard=y[random.randrange(3)]
        #fcard=add_Card()
        print(lcard)
        lname =faker.name()
        luid = randint(1000,1100)
        lost_list = Lost.objects.get_or_create(card=lcard,name=lname,uid=luid)
populate(20)