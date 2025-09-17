import uuid
from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pakaian', 'Pakaian'),
        ('aksesoris', 'Aksesoris'),
        ('alat pijat pria', 'Alat Pijat Pria'),
        ('perlengkapan olahraga', 'Perlengkapan Olahraga')

    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank= True, null=True)
    category = models.CharField(max_length=30, choices= CATEGORY_CHOICES, default='aksesoris')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    rating =  models.FloatField(default=0.0)
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def set_price(self,new_price):
        self.price = new_price
        self.save()

    
    def add_stock(self,new_stock):
        self.stock += new_stock
        self.save()



# Create your models here.
