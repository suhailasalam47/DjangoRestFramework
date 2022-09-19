from django.urls import path
from . import views


urlpatterns = [
    path('movielist/', views.movie_list),
    path('movie/<int:pk>/', views.movie_details),
]