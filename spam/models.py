from django.db import models

class spamdb(models.Model):
    name = models.CharField(max_length=20)
    data = models.CharField(max_length=5000)

