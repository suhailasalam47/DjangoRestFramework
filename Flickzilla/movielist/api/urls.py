from django.urls import path
from movielist.api import views


urlpatterns = [
    path('movielist/', views.WatchListAPI.as_view()),
    path('movie/<int:pk>/', views.WatchDetails.as_view()),
    path('stream/', views.StreamPlatformAPI.as_view()),
    path('stream/<int:pk>', views.StreamDetailAPI.as_view()),
]