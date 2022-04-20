from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])

class BankAccount(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    banckName= models.CharField(max_length=50)
    accountNumber= models.CharField(max_length= 15)
    balance=models.FloatField(default=0)
    
    """"Redondea balance en dos decimalestes de guardar en la DB"""
    def save(self, *args, **kwargs):
        self.balance = round(self.balance, 2)
        super(BankAccount, self).save(*args, **kwargs)

