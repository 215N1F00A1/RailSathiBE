from django.urls import path, include
from rest_framework import routers
from . import views
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),           # 👈 HTML view at /
    path('api/', include(router.urls)),            # 👈 API view at /items/api/items/
]
