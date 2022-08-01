from django.db import models
from rest_framework import routers, serializers, viewsets
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)
    published_year = models.CharField(max_length=255, blank=True,
                                      null=True)
    acquired = models.BooleanField(default=True)
    authors = models.TextField()
    thumbnail = models.TextField(blank=True)

    def __str__(self):
        return self.title


