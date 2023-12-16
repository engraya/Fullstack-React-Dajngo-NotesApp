from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['createdAt', 'updatedAt']


    def __str__(self):
        return self.title
    
    
