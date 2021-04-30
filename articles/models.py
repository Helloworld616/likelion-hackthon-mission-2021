from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)