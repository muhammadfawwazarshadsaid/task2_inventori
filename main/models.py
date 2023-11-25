from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)