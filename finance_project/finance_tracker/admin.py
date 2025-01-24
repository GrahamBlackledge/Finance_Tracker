from django.contrib import admin
from .models import Account, BudgetGoal, Transaction, Asset, Category
# Register your models here.
admin.site.register(Account)
admin.site.register(BudgetGoal)
admin.site.register(Transaction)
admin.site.register(Asset)
admin.site.register(Category)