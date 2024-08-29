from rest_framework import generics
from .models import Wish
from .serializers import WishSerializer


class WishListAPIView(generics.ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
