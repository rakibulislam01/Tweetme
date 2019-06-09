from django.urls import path

from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)  # tweet_detail_view, tweet_list_view

app_name = 'tweets'
urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),
]
