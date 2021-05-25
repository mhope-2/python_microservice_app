from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def __init__(self): 
        pass

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
