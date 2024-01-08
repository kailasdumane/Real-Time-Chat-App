from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, default="python")
    slug = models.SlugField(unique=True)
    




