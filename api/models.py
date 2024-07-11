# Models
# api/models.py

from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='project_images/')

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    images = models.ManyToManyField(Image)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()