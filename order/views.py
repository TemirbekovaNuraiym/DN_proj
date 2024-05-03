from rest_framework import viewsets


from .models import Order
from .serializers import OrderSerialezer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerialezer

    def get_serializer_context(self):
        return {'request': self.request}
    
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context
        return self.serializer_class(*args, **kwargs)
