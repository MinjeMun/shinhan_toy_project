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

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

# class CommentCreateView(
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     serializer_class = CommentSerializer

#     def get_queryset(self):
#         return Comment.objects.all()

#     def post(self, request, *args, **kwargs):
#         return self.create(request, args, kwargs)