from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
# Create your views here.

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'finance_tracker/transaction_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)