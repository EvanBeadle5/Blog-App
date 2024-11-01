from django.contrib import admin
from .models import Post

# Display posts in admin page.
admin.site.register(Post)