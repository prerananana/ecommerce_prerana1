
## Lab 3 : To add search fields and list display in brand, product and category




### Introduction

In our second lab, we created three models brand, category and product in product_module. Now, add the list display and search fields on each of the three models.

### Objectives

- To add list display, search field and list filter in product model
- To add list display and search field  in brand and category model
s
### Procedure

- **Adding the following code to product model of admin.py**

```
  class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    readonly_fields = ["quantity",]
  class Meta:
    model = Product
  admin.site.register(Product, ProductAdmin)
```
- **Adding the following code to brand model of admin.py**

```
  class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields =["name", "is_active",]
  class Meta:
    model = Brand
  admin.site.register(Brand, BrandAdmin)
```
- **Adding the following code to category model of admin.py**

```
  class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields =["name", "is_active",]
  class Meta:
    model = Category
  admin.site.register(Category, CategoryAdmin)
```
- **Adding the following code to product class of models.py to add a field 'image_tag'**

```
  ...
  from django.utils.html import mark_safe
  ...
  class Product(models.Model):
  ...
    def image_tag(self):
      return mark_safe(f'<img src="{self.image_url}" width="50"
      height="50" />')
      image_tag.short_description = "Product"
    def __str__(self):
      return self.name
```
- **Making the following changes in product model of admin.py to display the image tag**

```
  ...
  class ProductAdmin(admin.ModelAdmin):
    list_display=["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category","price",]
    # readonly_fields = ["quantity",]
  class Meta:
    model = Product
  admin.site.register(Product, ProductAdmin)
```

- **Finally, running the project and performing CRUD operations on Brand, Category and Product**

```
 python manage.py runserver
```

### Outputs

- **The Brand model**

![](/Labsheet/images_lab3/brand.png)

- **The Category model**

![](/Labsheet/images_lab3/category.png)

- **The Product model**

![](/Labsheet/images_lab3/products.png)

### Conclusion

As a result, we used multiple codes in this lab to create a search bar for products, brands, and categories, as well as display images for the products on the e-commerce site.
