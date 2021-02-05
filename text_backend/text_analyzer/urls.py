from django.urls import path
from . import views

urlpatterns = [
    path('headers/', views.headers, name='headers'),
    path('createTextObjects/', views.create_text_objects, name='createTextObjects'),
    path('twitter/recent/', views.compare_recent_tweets, name='recentTweets'),
    path('fromUsername/', views.id_and_text_from_user, name='fromUsername'),
    path('analyzeText/', views.analyze_text, name='analyzeText'),
    path('compareRawText/', views.compare_raw_text, name='compareRawText'),
]
