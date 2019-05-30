from django.urls import path
from .views import TweetListView, TweetDetailView, TweetCreateView   # tweet_detail_view, tweet_list_view

urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('1', TweetDetailView.as_view(), name='detail'),
]
