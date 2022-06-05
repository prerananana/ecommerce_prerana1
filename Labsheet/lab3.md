
## Lab 3 : To add search fields and list display in brand, product and category




### Introduction

In our first lab, we created a product module. Now, we add a brand, product and category in the product module which has a structure of the er diagram as shown below:

![Er diagram, the product module](/images_lab2/ER-product_module.png)
### Objectives

- To add Product, Brand and Category models
- To get more information about adding models and how models.py works
- To get more information about the admin.py, models.py as well as other files that django framework provides
- To perform CRUD operations on all three models

### Procedure

- **Adding the model Brand in the models.py**

```
  class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
```
- **Adding the model Category in the models.py**

```
  class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
  class Meta:
    verbose_name_plural = "Categories"
```
- **Adding the model Product in the models.py**

```
  class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
```
- **Making changes to the db by performing migrations**

```
  python manage.py makemigrations
  python manage.py migrate
```
- **Adding the following code to admin.py for enabling CRUD operations in the admin site**

```
  from .models import Brand, Category, Product
  admin.site.register(Brand)
  admin.site.register(Category)
  admin.site.register(Product)
```

- **Finally, running the project and performing CRUD operations on Brand, Category and Product**

```
 python manage.py runserver
```

### Outputs

- **Adding the models Brand, Category and Product**

![](/images_lab2/three_models.png)

- **The Brand model**

![](/images_lab2/brand.png)

![](/images_lab2/brand_detailed.png)

- **The Category model**

![](/images_lab2/category.png)

![](/images_lab2/category_detailed.png)

- **The Product model**

![](/images_lab2/product.png)

![](/images_lab2/productdetailed.png)

### Conclusion

Therefore, in our third lab we created the models Brand, Category and Product for our ecommerce site. All the three models inherits models.Model. The product and brand, category model are related to each other through one to many relationship. We have also used different data types provided by django. 
