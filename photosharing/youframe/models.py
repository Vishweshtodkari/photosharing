from django.db import models

# Create your models here.

class Destination(models.Model):

    
    img = models.ImageField(upload_to='pics')

