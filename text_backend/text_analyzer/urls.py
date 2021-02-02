from django.urls import path
from . import views

urlpatterns = [
    path('headers/', views.headers, name='headers'),
    path('textObjects/', views.create_text_objects, name='textObjects'),
    path('twitter/recent/', views.compare_recent_tweets, name='recentTweets')
]
