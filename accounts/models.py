from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    part_list = (
        ('기획디자인','기획디자인'),
        ('프론트엔드', '프론트엔드'),
        ('백엔드', '백엔드')
    )
    
    name = models.CharField(max_length=8)
    part = models.CharField(max_length=8, choices=part_list, default='백엔드')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name