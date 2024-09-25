from django.urls import path
from .views import WishListAPIView, WishDetailAPIView, WishReserveAPIView, AddWishesAPIView


urlpatterns = [
    path('api/wishes/', WishListAPIView.as_view(), name='wish-list'),
    path('api/wishes/add/', AddWishesAPIView.as_view(), name='add-wishes'),
    path('api/wishes/<int:id>/', WishDetailAPIView.as_view(), name='wish-detail'),
    path('api/wishes/<int:id>/reserve/', WishReserveAPIView.as_view(), name='wish-reserve'),
]