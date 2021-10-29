from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    facebook_id = models.URLField(blank=True)

    def __str__(self):
        return self.user.username