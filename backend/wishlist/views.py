from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wish
from .serializers import WishSerializer, WishAddSerializer


class WishListAPIView(generics.ListAPIView):
    serializer_class = WishSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wish.objects.filter(user=self.request.user)


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


class AddWishesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = WishAddSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
