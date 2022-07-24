# Ecommerce Lab 7
## Objective
For Payment Checkout Preparation, Invoice and Invoice Detail
## Introduction
In this lab of E-commerce we prepared for payment checkout and added invoice and invoice detail.
## Procedure
 1. First we add the code for invoice and invoice_detail in models.py.

        ...
        from django.contrib.auth.models import User
        from product_module.models import Product
        ...
        class Invoice(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        token = models.UUIDField()
        payment_date = models.DateTimeField()
        total_amount = models.FloatField()
        class InvoiceDetail(models.Model):
        invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField()
        sub_amount = models.FloatField()
 2. We added the following code to admin.py
   
        from .models import CartItem
        admin.site.register(CartItem)
        
  3. Then, we added view for cart and removecart.

  4. Under product_module, we make the following adjustments to urls.py

    from django.urls import path
    from .views import error_page, search, cart, removecart, success_page,
    error_page
    urlpatterns = [
    path('', search),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
    ]

  5. Under product_module and templates folder, we added “success.html” and "error.html".

        
## Outputs
![](/Labsheet/images_lab8&9/payment.png)

![](/Labsheet/images_lab8&9/invoice.png)

![](/Labsheet/images_lab8&9/invoice_details.png)

![](/Labsheet/images_lab8&9/payment_checkout.png)
## Conclusion
Therefore, in this lab we added invoice and invoice detail under payment_module and prepared for payment checkout.