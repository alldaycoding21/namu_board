from django.db import models

class User(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    published_date = models.DateTimeField(auto_now_add=True)