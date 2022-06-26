# Ecommerce Lab 4
## Objective
To create frontend for the website
## Introduction
In this lab of E-commerce we continued the lab by adding _index.html_ and _base.html_ to enhance the user interface of our e-commerce website.
## Procedure
 1. First we prepared template for Django and created a directory _templates_ and added a template for base file “base.html”.
 2. To make “templates/base.html”  globally available, we made following adjustment to _settings.py_
   
        TEMPLATES = [
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        
  3. We created a html file _index.html_ along with a directory _templates_ inside _product_module_
  4. We opened _views.py_ from the _product_module_ and added the code for search operation i.e. GET and POST .
  5. Then in  _product_module_ we created a file for _urls.py_ and added the URL routing config.
  
          from django.urls import path
          from .views import index
          urlpatterns = [
           path('', index),
          ]
  6. In *urls.py*, we included _product_module.urls_
  
            from django.contrib import admin
            from django.urls import path, include
            urlpatterns = [
             path('admin/', admin.site.urls),
             path('', include('product_module.urls')),
            ]
  7. Lastly we used the code _python manage.py runserver_ to run and generate outputs

  8. For template, we created a static folder and added the css, images and js files inside the static folder.

  9. We added ge following code in *settings.py* to implement static files

            STATIC_URL = 'static/'

            STATICFILES_DIRS = [
                BASE_DIR / "static",
            ]

10. We added the following static file path to href attribute

            {%static 'path' %}

## Outputs
![](/Labsheet/images_lab4/index_page1.png)

![](/Labsheet/images_lab4/index_page2.png)

## Conclusion
Therefore, in this lab we added base.html and index.html for the user end of our ecommerce website. I personally also added a bootstrap template and implemented it through static files.