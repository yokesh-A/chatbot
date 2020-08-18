from django.db import models

# Create your models here.

class dictionary(models.Model):
    question = models.TextField()
    keys = models.CharField(blank=True,max_length=200)
    answer = models.TextField(blank=True)
    usage = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)