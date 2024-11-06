from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
