from django.urls import path
from .views import WishListAPIView, WishDetailAPIView, WishReserveAPIView


urlpatterns = [
    path('api/wishes/', WishListAPIView.as_view(), name='wish-list'),
    path('api/wishes/<int:id>/', WishDetailAPIView.as_view(), name='wish-detail'),
    path('api/wishes/<int:id>/reserve/', WishReserveAPIView.as_view(), name='wish-reserve'),
]