from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Regular Django view for the homepage
def index(request):
    items_list = Item.objects.all()  # fetch items from DB
    return render(request, 'items/index.html', {'items': items_list})  # pass to template

# API view using Django REST Framework
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
