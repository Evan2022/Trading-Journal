from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    starting_balance = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Trade(models.Model):
    profit_loss = models.DecimalField(max_digits=15, decimal_places=2)
    time = models.TimeField()
    date = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

