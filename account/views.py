from django.shortcuts import render

from rest_framework.response import Response
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(srlf, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response('Вы успешно зарегистрировались', 201)


class ActivationView(APIView): 
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first() 
        if not user:
            return Response('Пользователь не найден', 404)
        user.activation_code = '' # стираем активационный код чтобы не загружать бд
        user.is_active = True # сделали аккаунт активным
        user.save()
        
        return Response('Вы успешно зарегистрировались', 201)
