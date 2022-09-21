from django.urls import path
from movielist.api import views


urlpatterns = [
    path('movielist/', views.WatchListAPI.as_view()),
    path('movie/<int:pk>/', views.WatchDetails.as_view(), name='watchlist-detail'),
    path('stream/', views.StreamPlatformAPI.as_view(), ),
    path('stream/<int:pk>', views.StreamDetailAPI.as_view(), name='streamplatform-detail'),
    path('review/', views.ReviewList.as_view(), name="review"),
    path('review/<int:pk>', views.ReviewDetails.as_view(), name="review-detail"),

]