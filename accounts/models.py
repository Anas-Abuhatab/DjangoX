from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField

class CustomUser(AbstractUser):
    name = CharField(max_length=64, null=True, blank=True)
    # owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # description =models.TextField()

    def __str__(self):
        return self.email