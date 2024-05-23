from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from finance.models import Deposit, Saving
# Create your models here.

class Portfolio(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='portfolios')
    birth = models.DateField(null=True, blank=True)
    household_size = models.PositiveIntegerField()
    MARITAL_STATUS_CHOICES = [
        ('single', '미혼'),
        ('married', '기혼'),
    ]
    marital_status = models.CharField(max_length=10, choices = MARITAL_STATUS_CHOICES)
    has_children = models.BooleanField(null=True, blank=True)
    income = models.DecimalField(max_digits=20, decimal_places=1)
    SAVINGS_CHOICES = [
        ('saving','적금'),
        ('deposit','예금'),
    ]
    savings = models.ManyToManyField(Saving, blank=True, related_name='savings')
    deposits = models.ManyToManyField(Deposit, blank=True, related_name='deposits')
    def __str__(self):
        return self.user.username
    
class SavingOption(models.Model):
    name = models.CharField(max_length=100)