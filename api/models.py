from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']


    def __str__(self):
        return self.title
    
    
