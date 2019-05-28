# from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=140)

    def __str__(self):
        return str(self.content)
