from django.db import models
from django.utils import timezone
# Create your models here.

class Company(models.Model):
    name = models.CharField(
        verbose_name='название компании',
        max_length=200
    )


    def __str__(self) -> str:
        return f'{self.name}'



class Shares(models.Model):
    date_create = models.DateTimeField(
        verbose_name='дата выпуска акции',
        default=timezone.now 
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=11,
        decimal_places=2,
        default=0
    )
    company = models.ForeignKey(
        verbose_name='какой компании принадлежит акция',
        related_name='company',
        to=Company,
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        verbose_name="кол-во акций",
        
    )
    is_available = models.BooleanField(
        verbose_name="Доступны для покупки",
        default=True  
    )
    def __str__(self) -> str:
        return f'{self.date_create}|{self.company}|{self.price}$|Осталось акций: {self.quantity}шт'
    
    def reduce_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            if self.quantity == 0:
                self.is_available = False
            self.save()