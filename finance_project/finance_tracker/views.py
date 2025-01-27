from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from django.urls import reverse_lazy
# Create your views here.

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'finance_tracker/transaction_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = 'category', 'transaction_type', 'amount', 'time_of_transaction', 'description', 'is_recurring'     
    template_name = 'finance_tracker/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

    def form_valid(self, form):
        form.instance,user =self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = 'category', 'transaction_type', 'amount', 'time_of_transaction', 'description'
    template_name = 'finance_tracker/transaction_form.html'
    success_url = reverse_lazy('transaction_list')
    
