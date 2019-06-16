from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView

from .views import (TweetListAPIView)

app_name = 'tweets-api'
urlpatterns = [
    url('', TweetListAPIView.as_view(), name='list')  # api/tweet/
]
