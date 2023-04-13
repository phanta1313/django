from django.db import models
from django.db.models import Sum



class product_category(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

class product_type(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

class category(models.Model):
    product_category = models.ForeignKey(product_category, default=None, on_delete=models.CASCADE)
    roduct_type = models.ForeignKey(product_type, default=None, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, default=None)
    product_price = models.IntegerField(default=None)
    def __str__(self):
        return self.product_name

price_sum = category.objects.aggregate(Sum('product_price'))
print(price_sum)


    


    

    
   

    
    
    
