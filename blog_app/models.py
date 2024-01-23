from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid


class Blog(models.Model):
    title = models.CharField(max_length=264,)
    content = models.TextField()
    slug = models.SlugField(max_length=264, unique=True, default=uuid.uuid1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
