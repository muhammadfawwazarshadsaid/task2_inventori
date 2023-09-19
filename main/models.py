from django.db import models

class Product(models.Model):
    no = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()