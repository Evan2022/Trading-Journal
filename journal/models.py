from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Journal(models.Model):
    SYMBOLS = {'USD': '$', 'EUR': '€', 'GBP': '£'}
    CURRENCY_CHOICE = (
        ('USD', SYMBOLS['USD']),
        ('EUR', SYMBOLS['EUR']),
        ('GBP', SYMBOLS['GBP']),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICE)
    name = models.CharField(max_length=200, unique=True)
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def symbol(self):
        return self.SYMBOLS.get(self.currency)


class Trade(models.Model):
    profit_loss = models.DecimalField(max_digits=15, decimal_places=2)
    time = models.TimeField()
    date = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    image_link = models.CharField(max_length=1000, blank=True, null=True) 
