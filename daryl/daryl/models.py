from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)

class Image(models.Model):
    filename = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey('Category')
