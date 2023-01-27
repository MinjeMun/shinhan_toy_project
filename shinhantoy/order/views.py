from rest_framework import generics, mixins
from .models import Order, Comment
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    OrderSerializer, 
    CommentCreateSerializer, 
    CommentDeleteSerializer,
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
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(self, request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        return Order.objects.all()
        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    pagination_class = OrderLargePagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer

    def get_permission_class(self):
        if self.request.method == 'POST':
            return [IsAuthenticated]
        return 

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(order_id = pk).order_by('-id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    serializer_class = CommentDeleteSerializer

    def get_queryset(self):
        member_id =  self.request.user.id
        return Comment.objects.filter(member_id=member_id).order_by('-id')

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)