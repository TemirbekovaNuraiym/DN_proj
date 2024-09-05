from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()



class Favorite(models.Model):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Пост')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления в избранное') 

    def __str__(self):
        return f'{self.product}'
