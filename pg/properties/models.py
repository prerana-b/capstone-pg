from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Postproperty(models.Model):
    pg_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
