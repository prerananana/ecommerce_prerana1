# Ecommerce Lab 6
## Objective
To prepare the cart
## Introduction
In this lab of E-commerce we continued the lab we added cart_item model, cart view and html for cart.
## Procedure
 1. First we added cart_item model to models .py

        ...
        from django.contrib.auth.models import User
        ...
        class CartItem(models.Model):
        user = models.ForeignKey(User , on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        entered_on = models.DateTimeField()

 2. Then we migated the model to ensure that the database table for added model is created sucessfully.
   
        python manage.py makemigrations product_module
        python manage.py migrate product_module
        
  3. Then, we registered the models to admin.py to ensure that the model is shown on the admin site.

    from .models import CartItem
    admin.site.register(CartItem)

  4. After this, we added the view for cart.
  5. We then created a cart.html to templates folder.
  6. We added the following code to urls.py to be able to redirect to cart.html

    from django.urls import path
    from .views import search, cart, removecart
    urlpatterns = [
    path('', search),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    ]
        
## Outputs
![](/Labsheet/images_lab6/cart.png)

![](/Labsheet/images_lab6/backcart.png)

## Conclusion
Therefore, in this lab we we added cart_item model, cart view and html for cart.