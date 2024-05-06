from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        models = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['images'] = ProductImg(instance.images.all(), many = True).data
        repr['category'] = CategorySerializer(instance.category).data['title']
        return repr
    
class ProductList(serializers.ModelSerializer): 
    class Meta: 
        models = Product
        fields = 'title','image', 'price', 'category',

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        models = Category
        fields = 'title',

class ProductImg(serializers.ModelSerializer): 
    class Meta: 
        models = ProductImage
        fields = 'image',

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta: 
        models = ProductImage
        fields = '__all__'
