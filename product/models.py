# product/models.py
from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты' 

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категории')
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, blank=True)
    image = models.ImageField(upload_to='products_img/', blank=True, verbose_name='Картинки')
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self): 
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_img/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Basket(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', blank=True, null=True)


    


