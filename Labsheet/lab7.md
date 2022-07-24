# Ecommerce Lab 7
## Objective
To define our payment gateway and pay via it.
## Introduction
In this lab of E-commerce we created a payment model in order to pay for the products in our ecommerce site.
## Procedure
 1. First create a payment_module.

        python manage.py startapp payment_module
 2. Then we added the payment_module to INSTALLED_APPS in settings.py
   
        INSTALLED_APPS = [ ...,
                'payment_module' ]
        
  3. In the payment_module, we added code for payment_gateway in “models.py”.

    import uuid
    class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4,editable=False)
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()

  4. To ensure database table for added model is created properly, we run the migrations.

    python manage.py makemigrations payment_module
    python manage.py migrate payment_module

  5. We then add the following code to admin.py
  
    from .models import PaymentGateway
    class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active",]
    class Meta:
    model = PaymentGateway
    admin.site.register(PaymentGateway, PaymentGatewayAdmin)
        
## Outputs
![](/Labsheet/images_lab7/payment.png)

## Conclusion
Therefore, in this lab we added our own payment gateway.