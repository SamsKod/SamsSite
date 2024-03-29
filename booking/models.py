from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import datetime
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    small_room = models.BooleanField(default=False)
    large_room = models.BooleanField(default=False)
    grand_room = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='media/profile_pics/IMG_0226_qhqn4c.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
