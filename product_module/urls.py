from django.urls import path
from .views import index, test, cart, removecart, success_page, error_page
urlpatterns = [
    path('', index),
    path('test', test),
    # path('index1', index1),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
]