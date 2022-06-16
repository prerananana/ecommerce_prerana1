from django.urls import path
from .views import index, test, index1
urlpatterns = [
    path('', index),
    path('test', test),
    path('index1', index1),
]