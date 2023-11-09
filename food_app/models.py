from django.db import models
import datetime
today = datetime.date.today()
year = today.year

# Create your models here.

class Category(models.Model):
    food_name = models.CharField(max_length=50) 
    pics = models.ImageField(upload_to='pics', default='')
    description = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.food_name
    

class Product(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    pics = models.ImageField(upload_to='product_pics')
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.product_name