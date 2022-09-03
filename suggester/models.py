from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=200)
