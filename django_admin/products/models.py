from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=256)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass
