from typing import Any
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager): # создание всех юзеров без разницы
    def _create_user(self, email, password, **extra):
        if not email: # ошибка при не указании email
            raise ValueError('укажите email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra) # достаем юзера
        user.set_password(password) #хешируем password (видоизменяем)
        user.save()
        return user
    

    def create_user(self, email, password, **extra): # создание обычного юзера
        user = self._create_user(email, password, **extra)
        user.create_activation_code() # активационный код
        user.save() # для добавления в БД
        return user
    

    def create_superuser(self, email, password, **extra): # создание суперюзера
        extra.setdefault('is_active', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True) # дали все привелегии 
        user = self._create_user(email, password, **extra) # создается юзер
        return user
    

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=11, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
        
    def __str__(self) -> str:
        return self.email
        
    def create_activation_code(self):
        code = get_random_string(length=11, 
                                     allowed_chars='0123456789')
        self.activation_code = code