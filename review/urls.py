from rest_framework.routers import DefaultRouter
from django.urls import path,include


from .views import FavoriteViewSet



router=DefaultRouter()
router.register('favorite', FavoriteViewSet)


urlpatterns=[
    path('',include(router.urls)),
]