import os
os.environ.setdefault('Django_settings_module','crudfbvproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

def populate(n):
    faker=Faker()
    for i in range(n):
        fnum = randint(1000,2000)
        fname =faker.name()
        fsal = randint(10000,20000)
        faddr = faker.city()
        emp_list = Employee.objects.get_or_create(enum=fnum,ename=fname,esal=fsal,eaddr=faddr)
populate(20)
                
        
        
        