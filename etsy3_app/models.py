from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    listing_id = models.IntegerField(null=True)
    

