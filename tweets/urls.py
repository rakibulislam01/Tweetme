from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)  # tweet_detail_view, tweet_list_view

app_name = 'tweets'
urlpatterns = [
    path('search', TweetListView.as_view(), name='list'),
    path('', RedirectView.as_view(url="/")),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),
]
