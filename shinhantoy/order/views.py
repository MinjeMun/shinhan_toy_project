from rest_framework import generics, mixins
from .models import Order, Comment

from .serializers import (
    OrderSerializer, 
    CommentCreateSerializer, 
    CommentSerializer
    )
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

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(order_id = pk)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)