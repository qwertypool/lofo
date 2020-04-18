import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','emprecords.settings')
import django
django.setup()
from testapp.models import employee
from faker import Faker
from random import *

fake=Faker()

def populate(n):
    for i in range(n):
        fakeid=fake.random_int(min=700,max=10000)
        fakename=fake.name()
        fakesal=fake.random_int(min=1000,max=100000)
        fakeaddr=fake.city()
        emp_info=employee.objects.get_or_create(empno=fakeid,empname=fakename,empsal=fakesal,empaddr=fakeaddr)
populate(10)
