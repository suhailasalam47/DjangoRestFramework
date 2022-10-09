from django.urls import path, include
from movielist.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream', views.StreamPlatformApi, basename="streamplatform")


urlpatterns = [
    path('movielist/', views.WatchListAPI.as_view()),
    path('movie/<int:pk>/', views.WatchDetails.as_view(), name='watchlist-detail'),
    path('', include(router.urls)),
    # path('stream/', views.StreamPlatformAPI.as_view(), ),
    # path('stream/<int:pk>', views.StreamDetailAPI.as_view(), name='streamplatform-detail'),
    path('stream/<int:pk>/review', views.ReviewList.as_view(), name="review"),
    path('stream/<int:pk>/create_review', views.CreateReview.as_view(), name="create_review"),
    path('stream/review/<int:pk>', views.ReviewDetails.as_view(), name="review-detail"),
    path('reviews/', views.ReviewUser.as_view(), name="review-user"),

]