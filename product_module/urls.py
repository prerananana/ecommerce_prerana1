from django.urls import path
from .views import index
urlpatterns = [
    path('', index),
    path('', include('product_module.urls')),
]