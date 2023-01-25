from rest_framework import generics, mixins

from .models import Order

from .serializers import OrderSerializer
from .paginations import OrderLargePagination


# Create your views here.

class OrderListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        return Order.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        return self.list(self, request, args, kwargs)
