from django.db import models
from accounts.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=32)
    content=models.TextField()

    def __str__(self):
        return f'{self.title}'
