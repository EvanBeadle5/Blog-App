from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#User profile.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', editable=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    #overwrite save function to auto-size images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        pfp = Image.open(self.profile_pic.path)
        
        if pfp.height > 300 or pfp.width > 300:
            pfp_size = (300, 300)
            pfp.thumbnail(pfp_size)
            pfp.save(self.profile_pic.path)