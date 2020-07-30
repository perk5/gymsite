from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    message = models.TextField(max_length=1000)
