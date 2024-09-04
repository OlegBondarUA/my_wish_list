from django.urls import path
from .views import WishListAPIView


urlpatterns = [
    path('api/wishes/', WishListAPIView.as_view(), name='wish-list'),
]