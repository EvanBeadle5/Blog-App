from django.db import models
from django.contrib.auth.models import User

#User profile.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(default='defaul.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'