from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def __init__(self): 
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def list(self, request): #/api/products/ -- GET
        pass

    def create(self, request): #api/products/ -- POST
        pass
    
    def retrieve(self, request, pk=None): #/api/products/<str: id> -- GET
        pass

    def update(self, request, pk=None): #/api/products/<str: id> -- GET
        pass

    def destroy(self, request, pk=None): #/api/products/<str: id> -- GET
        pass
