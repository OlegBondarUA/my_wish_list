from rest_framework import serializers
from .models import Wish


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'


class WishAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['id', 'name', 'image', 'description', 'link', 'price', 'achieved', 'reserved', 'added_at',
                  'reserved_at', 'user']
        read_only_fields = ['user']
