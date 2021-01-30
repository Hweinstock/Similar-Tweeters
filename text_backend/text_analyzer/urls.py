from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('headers/', views.headers, name='headers'),
    path('textObjects/', views.create_text_objects, name='textObjects')
]
