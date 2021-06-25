from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=40)
    source = models.CharField(max_length=300)
