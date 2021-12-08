from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse

class Snacks(models.Model):
    name = models.CharField(max_length=64)
    description= models.TextField()
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absloute_url(self):
        return reverse('snack_detail', args=[self.id])

    def __str__(self):
        return self.name