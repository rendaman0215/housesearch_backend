from django.db import models

class MakerCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='')