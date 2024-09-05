from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Category, Product, ProductImage, Basket
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, BasketSerializer

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Basket, Product
from django.contrib.auth.decorators import login_required



class PermissionMixin:
    def get_permissions(self): 
        if self.action in ('retrieve', 'list'):
            permissions = [AllowAny]
        else: 
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]
    

class CategoryViewSet(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(PermissionMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def get_serializer_class(self):
        if self.action == 'list': 
            return ProductSerializer
        return self.serializer_class
    
    
class ProductImageView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]



class AddToBasketView(APIView):
    def post(self, request, product_id):
        user = request.user
        product = get_object_or_404(Product, id=product_id)
        basket_item, created = Basket.objects.get_or_create(user=user, product=product)
        quantity = request.data.get('quantity', 1) 
        if not created:
            basket_item.quantity += int(quantity)
        else:
            basket_item.quantity = int(quantity)
        
        basket_item.price = basket_item.quantity * product.price
        basket_item.save()

        return Response({'message': 'Продукт удачно добавлен в корзину', 'basket': BasketSerializer(basket_item).data}, status=status.HTTP_200_OK)














