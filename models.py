from django.db import models

# Create your models here.
from module_account.models import User
from products.models import product

class basket(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    final=models.BooleanField(default=False)
    date=models.DateField()
    def __str__(self):
        return str(self.user)

class order(models.Model):
    basket=models.ForeignKey(basket,on_delete=models.CASCADE)
    title=models.ForeignKey(product,on_delete=models.CASCADE)
    def __str__(self):
        return f"product name : {self.title} - basket : {self.basket}"