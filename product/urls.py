# product/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageView
from .views import AddToBasketView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),  
    path('product-images/', ProductImageView.as_view(), name='product-image-create'),
    path('basket/add/<int:product_id>/', AddToBasketView.as_view(), name='add-to-basket')
]
