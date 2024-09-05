from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from .permissions import IsOwnerorReadOnly
from .models import Favorite
from .serializers import FavoriteSerializer




class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer  

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]  # Доступ только зарегистрированным пользователям
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerorReadOnly]  # Доступ только владельцам избранных товаров
        return [permission() for permission in self.permission_classes]
