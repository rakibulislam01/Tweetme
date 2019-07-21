from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    UserDetailView,
    UserFollowView
)  # tweet_detail_view, tweet_list_view

app_name = 'profiles'
urlpatterns = [
    path('<username>/', UserDetailView.as_view(), name='detail'),
    path('<username>/follow', UserFollowView.as_view(), name='follow'),
]
