from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
	filename = models.CharField(max_length=255, null=True, blank=True)
	category = models.CharField(max_length=255, null=True, blank=True)

class Category(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	category_id = models.PositiveIntegerField(null=True)