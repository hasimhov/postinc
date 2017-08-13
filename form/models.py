# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	image = models.ImageField(blank=True,upload_to="form/static/images")
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=30,primary_key=True)
	desig = models.CharField(max_length=25)
	skills = models.CharField(max_length=50)
	edu = models.CharField(max_length=30)
	about = models.CharField(max_length=100)
	locations = models.CharField(max_length=30)
