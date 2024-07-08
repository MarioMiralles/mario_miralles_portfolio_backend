# Models
# api/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
