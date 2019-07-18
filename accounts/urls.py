from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView
)  # tweet_detail_view, tweet_list_view

app_name = 'profiles'
urlpatterns = [
    path('<username>/', UserDetailView.as_view(), name='detail'),
]
