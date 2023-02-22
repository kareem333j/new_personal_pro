from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=20, default="Title", blank=True)
    post_value = models.CharField(max_length=1000)
    post_time = models.DateTimeField(default=datetime.now)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.post_title