# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse

from .validators import validate_content


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-timestamp']

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "":
    #         raise ValidationError("Conn't be blank")
    #     return super(Tweet, self).clean(*args, **kwargs)
