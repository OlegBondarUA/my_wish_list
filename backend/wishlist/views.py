from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wish
from .serializers import WishSerializer


class WishListAPIView(generics.ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class WishDetailAPIView(generics.RetrieveAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    lookup_field = 'id'


class WishReserveAPIView(APIView):
    def post(self, request, id, *args, **kwargs):
        wish = get_object_or_404(Wish, id=id)
        if not wish.reserved:
            wish.reserved = True
            wish.save()
            return Response({'status': 'Wish reserved'}, status=status.HTTP_200_OK)
        return Response({'status': 'Wish already reserved'}, status=status.HTTP_400_BAD_REQUEST)