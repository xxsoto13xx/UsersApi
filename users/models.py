from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        def __str__(self):
            return self.username
