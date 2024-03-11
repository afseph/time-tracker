from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length = 255)
    time_elapsed = models.CharField(max_length = 255, default="")
    session_id = models.CharField(max_length = 255, default="")