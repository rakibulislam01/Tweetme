from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView

from .views import (TweetListAPIView,
                    TweetCreateAPIView)

app_name = 'tweets-api'
urlpatterns = [
    url('list', TweetListAPIView.as_view(), name='list'),  # api/tweet/
    url('create', TweetCreateAPIView.as_view(), name='create')  # api/tweet/
]
