from django.urls import path
from movielist.api import views


urlpatterns = [
    path('movielist/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetails.as_view()),
]