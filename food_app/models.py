from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    food_name = models.CharField(max_length=50) 
    pics = models.ImageField(upload_to="category_pics")
    description = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.food_name
    

class Product(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    pics = models.ImageField(upload_to="product_pics")
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.product_name
    
    
class User(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    # ignore the username field it only for the superusers
    username = models.CharField(unique=False, max_length=100, null=True, default='')
    address = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(null=True, upload_to="profile_pics", default="profile_pics/avatar.png")
    joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
    

class Home_Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(
        validators=[EmailValidator(message="Invalid email address")]
    )
    message =  models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
 
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.email}"
   
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    paid = models.BooleanField(default=False)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order {self.order.id}"
