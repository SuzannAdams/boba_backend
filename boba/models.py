from django.db import models

# Create your models here.
class Meet(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    photo_url = models.TextField()
    def __str__(self):
        return self.name
