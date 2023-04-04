from django.db import models
from apps.users.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="post_user"
    )
    title = models.CharField(
        max_length=255
    )
    description = models.CharField(
        max_length=255
    )
    image = models.ImageField(
        upload_to="post_image/"
    )
    