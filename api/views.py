from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cloths, Cart, Order
from .serializers import ClothSerializer, CartSerializer, OrderSerializer
from rest_framework import status, permissions, generics


# Create your views here.

# product list

class ListCloths(generics.ListCreateAPIView):
    queryset = Cloths.objects.all()
    serializer_class = ClothSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClothSerializer(queryset, many=True)
        return Response(serializer.data)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothSerializer(queryset, many=False)
        return Response(serializer.data)


class UpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cloths.objects.all()
    serializer_class = ClothSerializer


class DeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cloths.objects.all()
    serializer_class = ClothSerializer

class AddToCartView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product=Cloths.objects.get(id=product_id)
            cart_item = Cart(user=request.user,product=product,quantity=quantity)
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error":"Product not found"},status=status.HTTP_404_NOT_FOUND)


class PaymentView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
