import django 
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

import faker
from random import * 
from math import *

f = faker.Faker()
from projectapp .models import student

def generate_data(n):
    for i in range(n):
        fname = f.name()
        fid = f.random_int(min = 10 , max = 100)
        fmarks = f.random_int(min = 10 , max = 100)

        student_list = student.objects.get_or_create(sid=fid, fname=fname, fmarks=fmarks)

    generate_data(10)