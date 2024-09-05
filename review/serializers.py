from rest_framework import serializers
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        exclude=['user']

    def validate(self, attrs):
        super().validate(attrs)
        request=self.context.get('request')
        attrs['user']=request.user 
        return attrs