from django.db import models


class Account(models.Model):
    ACCOUNT_TYPES = [
        ('CHK', 'Checking'),
        ('SVG', 'Saving'),
        ('CC', 'Credit Card'),
    ]
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    