from django.shortcuts import render
from rest_framework.response import Response

from .models import Cloths
from .serializers import ClothSerializer
from rest_framework import generics, status


# Create your views here.

# product list

class ListCloths(generics.ListCreateAPIView):
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ClothSerializer(queryset,many=True)
        return Response(serializer.data)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClothSerializer
    queryset = Cloths.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothSerializer(queryset,many=False)
        return Response(serializer.data)

