from django.db import models

# Create your models here.
class category(models.Model):
    name= models.CharField(max_length=32)
    description= models.CharField(max_length=120)
