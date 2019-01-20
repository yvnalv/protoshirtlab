from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SLUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)

class AdminUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    portofolio = models.URLField(blank=True)
    user_pics = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username
