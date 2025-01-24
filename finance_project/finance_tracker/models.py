from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return f"{self.name} {self.account_type} account for {self.user} balance is: {self.balance} "

class Category(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
    
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    time_of_transaction = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.time_of_transaction}"

class Asset(models.Model):
    ASSET_TYPES =[
        ('investment', 'Investment'),
        ('digital', 'Digital'), 
    ]
    type = models.CharField(max_length=30, choices=ASSET_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.type} asset, {self.amount} amount, worth: {self.value}"

class BudgetGoal(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} for {self.category} in {self.account}"
