from django.db import models
import random
import string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Rooms.objects.filter(code=code).count() == 0:
            break
    return code


class Rooms(models.Model):
    public = models.BooleanField()
    typeofmusic = models.CharField(max_length=2)
    size = models.CharField(max_length=1000)
    guestcanpause = models.BooleanField()
    description = models.CharField(max_length=1000)
    date = models.DateField()
    code = models.CharField(max_length=8, default="", unique=True)

    def __str__(self):
        return self.code
